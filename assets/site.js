/* Webcattus Labs — site script. No dependencies. */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     CONFIG: the only things you should need to edit.
     ------------------------------------------------------------------ */
  var CONFIG = {
    // Lead Router form endpoint (Cloudflare Worker).
    leadEndpoint: "https://lead-router.webcattus.workers.dev/form/webcattus",
    // Your scheduling link. Until it's set, the success screen promises an email with times instead.
    calendlyUrl: "https://calendly.com/YOUR-HANDLE/ai-readiness-audit",
    // Hosts where the form really submits. Anywhere else (a preview), it simulates success.
    liveHosts: ["webcattuslabs.com", "www.webcattuslabs.com", "localhost", "127.0.0.1"],
    email: "hello@webcattuslabs.com"
  };
  var calendlyReady = CONFIG.calendlyUrl.indexOf("YOUR-HANDLE") === -1;

  var ES = (document.documentElement.lang || "en").slice(0, 2) === "es";
  var T = ES ? {
    openMenu: "Abrir menú", closeMenu: "Cerrar menú", copied: "Copiado", perWeek: " / semana",
    sending: "Enviando… ", submit: "Enviar y elegir horario ", noMessage: "(Sin mensaje)",
    invalid: "Necesitamos un teléfono o correo electrónico válido.",
    tooMany: "Ya nos envió varias solicitudes. Escríbanos a " + CONFIG.email + ".",
    failed: "No pudimos enviarlo en este momento. Inténtelo de nuevo o escríbanos a " + CONFIG.email + ".",
    hello: function (n) { return "Gracias, " + n + ". Recibimos sus datos."; }
  } : {
    openMenu: "Open menu", closeMenu: "Close menu", copied: "Copied", perWeek: " / week",
    sending: "Sending… ", submit: "Send and pick a time ", noMessage: "(No message)",
    invalid: null,
    tooMany: "You've sent a few requests already. Please email us at " + CONFIG.email + ".",
    failed: "We couldn't send that just now. Please try again, or email " + CONFIG.email + ".",
    hello: function (n) { return "Thanks, " + n + ". Your details are in."; }
  };

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  /* ---------- header: shadow on scroll, mobile menu ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.getElementById("nav-menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? T.closeMenu : T.openMenu);
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) { menu.classList.remove("is-open"); toggle.setAttribute("aria-expanded", "false"); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open"); toggle.setAttribute("aria-expanded", "false"); toggle.focus();
      }
    });
  }

  /* ---------- footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = String(new Date().getFullYear()); });

  /* ---------- copy buttons ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () { var t = btn.textContent; btn.textContent = T.copied; setTimeout(function () { btn.textContent = t; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { selectSibling(btn); });
      } else { selectSibling(btn); }
    });
  });
  function selectSibling(btn) {
    var code = btn.parentNode.querySelector("code");
    if (!code) return;
    var r = document.createRange(); r.selectNodeContents(code);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }

  /* ---------- missed-revenue calculator ---------- */
  var calc = document.getElementById("calc");
  if (calc) {
    var money = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });
    var inputs = {
      missed: document.getElementById("calc-missed"),
      rate: document.getElementById("calc-rate"),
      value: document.getElementById("calc-value")
    };
    var outs = {
      missed: document.getElementById("out-missed"),
      rate: document.getElementById("out-rate"),
      value: document.getElementById("out-value"),
      month: document.getElementById("out-month"),
      year: document.getElementById("out-year")
    };
    var update = function () {
      var missed = Number(inputs.missed.value);
      var rate = Number(inputs.rate.value) / 100;
      var value = Number(inputs.value.value);
      var month = missed * (52 / 12) * rate * value;
      outs.missed.value = missed + T.perWeek;
      outs.rate.value = Math.round(rate * 100) + "%";
      outs.value.value = money.format(value);
      outs.month.textContent = money.format(month);
      outs.year.textContent = money.format(month * 12);
    };
    Object.keys(inputs).forEach(function (k) { inputs[k].addEventListener("input", update); });
    update();
  }

  /* ---------- booking form → Lead Router → scheduling ---------- */
  var form = document.getElementById("booking-form");
  if (!form) return;

  var card = form.closest(".form-card");
  var booked = card.querySelector(".booked");
  var status = form.querySelector(".form-status");
  var button = form.querySelector('button[type="submit"]');
  var steps = card.querySelectorAll(".progress .pill");
  var opened = Date.now();
  var isLive = CONFIG.liveHosts.indexOf(location.hostname) !== -1;

  // The no-JS round trip comes back with ?sent=1 / ?sent=0.
  var sentParam = new URLSearchParams(location.search).get("sent");
  if (sentParam === "1") showBooked({});
  if (sentParam === "0") showError(null);

  function checkedValues(name) {
    return Array.prototype.map.call(form.querySelectorAll('input[name="' + name + '"]:checked'), function (i) { return i.value; });
  }
  function val(name) {
    var el = form.elements[name];
    return el ? String(el.value || "").trim() : "";
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    status.hidden = true;
    if (!form.checkValidity()) { form.reportValidity(); return; }

    var drains = checkedValues("drains");
    var qual = [
      ["Industry", val("industry")],
      ["Team size", val("team_size")],
      ["Biggest time drains", drains.join(", ")],
      ["Budget for a first project", val("budget")],
      ["Timeline", val("timeline")],
      ["Website", val("site_url")],
      ["Site language", ES ? "Spanish" : ""]
    ].filter(function (p) { return p[1]; }).map(function (p) { return p[0] + ": " + p[1]; });

    var body = new URLSearchParams();
    body.set("name", val("name"));
    body.set("email", val("email"));
    body.set("phone", val("phone"));
    body.set("company", val("company"));
    body.set("service", drains[0] || val("industry") || "AI Readiness Audit");
    body.set("message", (val("message") || T.noMessage) + (qual.length ? "\n\n" + qual.join("\n") : ""));
    body.set("website_hp", val("website_hp"));
    body.set("_elapsed", String(Date.now() - opened));

    button.disabled = true;
    button.firstChild.textContent = T.sending;

    if (!isLive) {
      // Preview: never posts. Shows the real success screen so the flow can be reviewed.
      setTimeout(function () { showBooked({ name: val("name"), email: val("email"), preview: true }); }, 600);
      return;
    }

    // URL-encoded body keeps this a CORS "simple" request (no preflight).
    fetch(CONFIG.leadEndpoint, { method: "POST", body: body })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { return { r: r, d: d }; }); })
      .then(function (x) {
        if (x.r.ok && x.d.ok) { showBooked({ name: val("name"), email: val("email") }); return; }
        if (x.r.status === 422 && x.d.error) { showError(T.invalid || x.d.error); return; }
        if (x.r.status === 429) { showError(T.tooMany); return; }
        showError(null);
      })
      .catch(function () { showError(null); });
  });

  function showError(text) {
    status.textContent = text || T.failed;
    status.hidden = false;
    button.disabled = false;
    button.firstChild.textContent = T.submit;
  }

  function showBooked(info) {
    form.hidden = true;
    booked.hidden = false;
    if (steps.length === 2) { steps[0].classList.remove("is-current"); steps[0].classList.add("is-done"); steps[1].classList.add("is-current"); }
    var first = (info.name || "").split(" ")[0];
    var hi = booked.querySelector("[data-hello]");
    if (hi && first) hi.textContent = T.hello(first);
    var cal = booked.querySelector("[data-calendar]");
    var noCal = booked.querySelector("[data-no-calendar]");
    if (calendlyReady && cal) {
      var url = new URL(CONFIG.calendlyUrl);
      if (ES) url.searchParams.set("locale", "es");
      if (info.name) url.searchParams.set("name", info.name);
      if (info.email) url.searchParams.set("email", info.email);
      cal.href = url.toString();
      cal.hidden = false;
      if (noCal) noCal.hidden = true;
    }
    var prev = booked.querySelector("[data-preview]");
    if (prev) prev.hidden = !info.preview;
    booked.focus({ preventScroll: false });
  }
})();
