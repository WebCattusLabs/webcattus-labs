"""Page copy and layout for the Webcattus Labs site. Edit text here, then run build.py."""
import html as _html
from build import I, CONTACT, EMAIL, PHONE_E164, PHONE_DISPLAY, closer, call_button

A = I["arrow"]

def fix_bullets(items):
    return "<ul>" + "".join(f'<li>{I["check"]}<span>{t}</span></li>' for t in items) + "</ul>"

def check_list(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f'<li>{I["check"]}<span>{t}</span></li>' for t in items) + "</ul>"

# ======================================================================== HOME
HOME = f'''
<section class="hero aurora" aria-labelledby="hero-title">
  <div class="grid-lines" aria-hidden="true"></div>
  <div class="wrap hero__grid">
    <div class="hero__copy">
      <p class="label rise">AI consulting for small business · Dallas–Fort Worth</p>
      <h1 id="hero-title" class="rise rise-2">AI that wins back your <em>hours</em> and your missed customers.</h1>
      <p class="lead rise rise-3">Webcattus Labs helps small business owners automate the follow-ups, admin and customer questions that eat their week. Before we build anything, we agree on a target in hours saved or revenue recovered, and we report against it every month.</p>
      <div class="cta-row rise rise-4">
        <a class="btn btn--primary" href="{CONTACT}">Book an AI Readiness Audit {A}</a>
        <a class="btn btn--ghost" href="#how">See how it works</a>
      </div>
      <p class="cta-note rise rise-4"><span>Free 30-minute call</span><span>No prep needed</span><span>Plain-English answers</span></p>
      <p class="small muted rise rise-4">Prefer to talk now? Call <a href="tel:{PHONE_E164}"><b>{PHONE_DISPLAY}</b></a></p>
    </div>

    <figure class="console rise rise-5" aria-label="Illustration: how a missed call is handled by an AI follow-up system">
      <div class="console__bar">
        <span class="console__title">Missed call → booked job</span>
        <span class="tag">Example</span>
      </div>
      <ol class="timeline">
        <li><time>7:42 PM</time><span class="dot">{I["phone"]}</span><div><strong>Missed call during dinner rush</strong><span>(214) •••-0142 · first-time caller</span></div></li>
        <li><time>7:42 PM</time><span class="dot dot--accent">{I["msg"]}</span><div><strong>Text sent to the caller</strong><span>"Sorry we missed you. What can we help with?"</span></div></li>
        <li><time>7:43 PM</time><span class="dot dot--accent">{I["bell"]}</span><div><strong>Routed to Maria, on call tonight</strong><span>Caller replied: "Catering for 40 on Saturday"</span></div></li>
        <li><time>7:47 PM</time><span class="dot dot--good">{I["user"]}</span><div><strong>Maria claimed it and called back</strong><span>No one else was pinged</span></div></li>
        <li><time>7:58 PM</time><span class="dot dot--good">{I["check"]}</span><div><strong>Booked: Saturday catering, 40 guests</strong><span>Logged with outcome for the monthly report</span></div></li>
      </ol>
      <figcaption class="console__foot"><span>Time to first reply <b>under 1 min</b></span><span>Owner involvement <b>none</b></span></figcaption>
    </figure>
  </div>
</section>

<section class="creds" aria-label="Founder credentials">
  <div class="wrap">
    <p class="creds__label">The credentials behind every build</p>
    <ul>
      <li>{I["badge"]}Google Cloud Professional Data Engineer</li>
      <li>{I["badge"]}Google Cloud Professional Cloud Architect</li>
      <li>{I["badge"]}Databricks Data Engineer Professional</li>
      <li>{I["badge"]}PMP® certified</li>
      <li>{I["book"]}12 peer-reviewed publications</li>
      <li>{I["award"]}Springer Best Paper Award, 2026</li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="pain-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">The problem</p>
      <h2 id="pain-title">Small businesses don't lose to bigger competitors. They lose to slower ones.</h2>
      <p class="lead">Most small businesses have the same three leaks. None of them need a new hire. All of them can be fixed with well-set-up AI.</p>
    </div>
    <div class="pains">
      <div class="pain"><p class="stat">The first reply wins.</p><p>A customer who can't reach you calls the next business on the list. Calls missed during a rush and forms that sit until morning are revenue walking out the door.</p></div>
      <div class="pain"><p class="stat">The 9 PM admin shift.</p><p>Quotes, follow-ups, scheduling, data entry and the same five customer questions. The owner ends up doing them after closing, every night.</p></div>
      <div class="pain"><p class="stat">Tools that don't talk.</p><p>The phone, the inbox, the booking app and the spreadsheet each hold part of the picture. Things fall through the gaps between them.</p></div>
    </div>
  </div>
</section>

<section class="section section--tint" aria-labelledby="services-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">What we do</p>
      <h2 id="services-title">Four ways we put AI to work for you</h2>
      <p class="lead">Start with a plan, automate the work that matters most, and make sure your team actually uses it.</p>
    </div>
    <div class="grid-4">
      <a class="card card-link" href="services.html#workshop">
        <span class="icon">{I["compass"]}</span><h3>AI Strategy</h3>
        <p>Find the two or three tasks where AI pays off fastest, with a cost and payback estimate for each.</p>
        <p class="result">Typical outcome: <b>a 90-day roadmap you can act on</b></p>
        <span class="more">AI Discovery Workshop {A}</span>
      </a>
      <a class="card card-link" href="services.html#agents">
        <span class="icon">{I["flow"]}</span><h3>Workflow Automation</h3>
        <p>Lead follow-up, scheduling, intake and reporting run on their own and hand off to a person when it matters.</p>
        <p class="result">Typical target: <b>5–10 hours back each week</b></p>
        <span class="more">Custom AI Agents {A}</span>
      </a>
      <a class="card card-link" href="services.html#agents">
        <span class="icon">{I["chat"]}</span><h3>Custom AI Assistants</h3>
        <p>Assistants trained on your menus, prices and policies that answer customers and staff accurately, around the clock.</p>
        <p class="result">Typical target: <b>replies in minutes, not hours</b></p>
        <span class="more">Custom AI Agents {A}</span>
      </a>
      <a class="card card-link" href="services.html#training">
        <span class="icon">{I["users"]}</span><h3>Team AI Training</h3>
        <p>Hands-on sessions built around your team's real tasks, so AI tools get used safely every day instead of once.</p>
        <p class="result">Typical outcome: <b>a shared playbook your team keeps</b></p>
        <span class="more">Team AI Training {A}</span>
      </a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ind-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Problems we fix</p>
      <h2 id="ind-title">If it slows your business down, we can probably fix it.</h2>
      <p class="lead">These are the bottlenecks we see most in restaurants, home-services companies and construction firms. We set up the fix, train your team, and make sure it keeps working.</p>
    </div>
    <div class="ind-cols">
      <div class="ind-col">
        <h3><span class="icon">{I["plate"]}</span>Restaurants</h3>
        {fix_bullets(["Catering and private-event inquiries that never sit unanswered", "Review responses drafted in your voice", "Missed-call text-back during the dinner rush", "Hours and menu kept consistent on Google, Yelp and your site", "No-show reminders, shift coverage and a morning sales text"])}
        <a class="more" href="industries.html#restaurants">Every restaurant fix {A}</a>
      </div>
      <div class="ind-col">
        <h3><span class="icon">{I["thermo"]}</span>HVAC &amp; home services</h3>
        {fix_bullets(["Unsold estimates followed up automatically", "After-hours calls booked or sent to the on-call tech", "Maintenance agreements renewed before they lapse", "Voice notes turned into job notes and invoices", "Review requests after every completed job"])}
        <a class="more" href="industries.html#home-services">Every home-services fix {A}</a>
      </div>
      <div class="ind-col">
        <h3><span class="icon">{I["hardhat"]}</span>Construction</h3>
        {fix_bullets(["Daily logs and progress reports from site photos and voice notes", "Change orders drafted and sent for signature the same day", "Subcontractor insurance certificates tracked before they expire", "Weekly homeowner updates without the phone calls", "Overdue invoices and lien waivers chased on schedule"])}
        <a class="more" href="industries.html#construction">Every construction fix {A}</a>
      </div>
    </div>
    <div class="mid-cta"><p>Don't see your problem? Tell us about it. Most of what we build is custom.</p>
      <div class="cta-row">{call_button("btn btn--primary")}<a class="btn {"btn--ghost" if PHONE_E164 else "btn--primary"}" href="{CONTACT}">Book a free consultation {A}</a></div></div>
  </div>
</section>

<section class="section section--tint" aria-labelledby="calc-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Do the math</p>
      <h2 id="calc-title">What are slow replies costing you?</h2>
      <p class="lead">Move the sliders to match your business. The math runs in your browser and nothing is sent anywhere.</p>
    </div>
    <div class="calc" id="calc">
      <div class="calc__inputs">
        <div class="calc__field">
          <div class="calc__row"><label for="calc-missed">Inquiries missed or answered late</label><output id="out-missed" for="calc-missed">8 / week</output></div>
          <input id="calc-missed" type="range" min="1" max="40" step="1" value="8">
          <p class="calc__hint">Missed calls, voicemails, and forms that waited more than an hour.</p>
        </div>
        <div class="calc__field">
          <div class="calc__row"><label for="calc-rate">Share you'd win with a fast reply</label><output id="out-rate" for="calc-rate">25%</output></div>
          <input id="calc-rate" type="range" min="5" max="60" step="5" value="25">
          <p class="calc__hint">Be conservative. One in four is a sensible starting point.</p>
        </div>
        <div class="calc__field">
          <div class="calc__row"><label for="calc-value">Average sale or job value</label><output id="out-value" for="calc-value">$400</output></div>
          <input id="calc-value" type="range" min="50" max="5000" step="50" value="400">
          <p class="calc__hint">A typical order, ticket or first invoice.</p>
        </div>
      </div>
      <div class="calc__result" aria-live="polite">
        <p class="label">Revenue at risk</p>
        <p class="calc__big" id="out-month">$3,467</p>
        <p class="calc__year">per month, or about <b id="out-year">$41,600</b> a year</p>
        <p class="small">An estimate from your inputs, not a promise. In the audit we check it against your real call and inquiry data.</p>
        <a class="btn btn--light" href="{CONTACT}">Check my real numbers {A}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="how" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">How it works</p>
      <h2 id="how-title">From first call to measurable results in about a month</h2>
    </div>
    <ol class="steps">
      <li class="step"><h3>Find the leak</h3><p class="when">Free audit, then week 1</p>
        <p>A 30-minute AI Readiness Audit, then an optional one-day workshop. We map where time and customers slip away and agree on one target number.</p></li>
      <li class="step"><h3>Build it with guardrails</h3><p class="when">Weeks 2–4</p>
        <p>We set up the automation inside the tools you already use, test it on real examples from your business, and train your team before it goes live.</p></li>
      <li class="step"><h3>Measure and improve</h3><p class="when">Every month</p>
        <p>A short report on hours saved, replies sent and jobs booked against the target. We tune what's working and switch off what isn't.</p></li>
    </ol>
  </div>
</section>

<section class="section section--tint" aria-labelledby="proof-title">
  <div class="wrap proof">
    <div class="stack">
      <p class="label">Proof, not promises</p>
      <h2 id="proof-title">We run our own business on what we sell.</h2>
      <p class="lead">Every inquiry sent to Webcattus Labs, including the form on this site, goes through Lead Router, the same follow-up system we set up for clients. Nothing waits in an inbox.</p>
      {check_list([
        "Every call and form is logged, sorted and sent to the right person's phone",
        "If nobody claims it, it escalates automatically until someone does",
        "Each lead's outcome is recorded, so the monthly report shows booked work, not activity",
        "Safety-sensitive or unclear requests always go to a person, never to AI alone",
      ])}
      <div class="cta-row"><a class="btn btn--ghost" href="use-cases.html">See the use cases {A}</a></div>
    </div>
    <div class="specs" aria-label="Lead Router facts">
      <div class="spec"><b>Seconds</b><span>from a new inquiry to an alert on your phone</span></div>
      <div class="spec"><b>10 min</b><span>default wait before an unclaimed lead escalates</span></div>
      <div class="spec"><b>8:00 AM</b><span>daily summary of every lead and what happened</span></div>
      <div class="spec"><b>48</b><span>automated tests run before every change goes live</span></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="trust-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Responsible by design</p>
      <h2 id="trust-title">AI you can trust with your customers</h2>
      <p class="lead">The question isn't whether AI can do the task. It's whether you can trust it with your reputation. These rules come with every build.</p>
    </div>
    <div class="principles">
      <div class="principle"><span class="icon">{I["hand"]}</span><h3>A person approves what matters</h3><p>Prices, promises, complaints and anything safety-related go to a human. AI drafts; your team decides.</p></div>
      <div class="principle"><span class="icon">{I["lock"]}</span><h3>Your data stays yours</h3><p>We use business-grade AI plans that don't train on your data, and we only connect what the job needs.</p></div>
      <div class="principle"><span class="icon">{I["info"]}</span><h3>It knows when it doesn't know</h3><p>Assistants answer from your approved information. When they're unsure, they hand off instead of guessing.</p></div>
      <div class="principle"><span class="icon">{I["key"]}</span><h3>You own everything</h3><p>Accounts, data and setups live in your name. If we part ways, everything keeps working without us.</p></div>
    </div>
    <p class="muted small" style="margin-top:2rem">Works with the tools you already use, including Google Workspace, Microsoft 365, Slack, Teams, Square, Shopify, QuickBooks and HubSpot.</p>
  </div>
</section>

{closer()}
'''

# ==================================================================== SERVICES
SERVICES = f'''
<section class="page-hero aurora" aria-labelledby="svc-title">
  <div class="wrap">
    <p class="label">Services &amp; pricing</p>
    <h1 id="svc-title">Clear scope. Fixed prices. Results you can measure.</h1>
    <p class="lead">Every engagement starts with a free AI Readiness Audit. From there, most clients follow the same path: plan, build, then improve month to month. You can stop after any step.</p>
    <div class="cta-row"><a class="btn btn--primary" href="{CONTACT}">Book an AI Readiness Audit {A}</a><span class="muted small">Free · 30 minutes · You'll get a written summary</span></div>
  </div>
</section>

<section class="section" style="padding-top:clamp(2rem,1.5rem + 2vw,3rem)">
  <div class="wrap">

    <article class="offer" id="workshop" aria-labelledby="o1">
      <div class="offer__head">
        <p class="label">Plan</p>
        <h2 id="o1">1-Day AI Discovery Workshop</h2>
        <p class="lead">One focused day with you and your key people to find where AI saves the most time and money, and what it would take to get there.</p>
        <div class="price"><b>$1,500</b><span>flat fee · on-site in DFW or remote · credited toward your first build if you start within 60 days</span></div>
        <div class="meta"><span class="tag">{I["clock"].replace('aria-hidden="true"','aria-hidden="true" width="12" height="12"')} 1 day + report in 3 business days</span><span class="tag">Up to 6 attendees</span></div>
      </div>
      <div class="offer__body">
        <div><h3>What you get</h3>
        {check_list([
          "A map of your 10 most time-consuming workflows, with hours per week for each",
          "An opportunity list ranked by return: estimated hours saved, revenue impact, setup cost and running cost",
          "Tool recommendations that fit what you already use, with honest pros and cons",
          "A 90-day roadmap with one target metric agreed up front",
          "A risk and data-privacy check for each recommendation",
          "A written report and recording, delivered within 3 business days",
        ])}</div>
        <div><h3>Best for</h3><p class="muted">Owners who know AI could help but aren't sure where to start, or who've tried a few tools that never stuck.</p></div>
      </div>
    </article>

    <article class="offer" id="agents" aria-labelledby="o2">
      <div class="offer__head">
        <p class="label">Build</p>
        <h2 id="o2">Custom AI Agent Deployment</h2>
        <p class="lead">We build, connect and launch an AI agent that takes one workflow off your plate end to end, with a person in control at every step that matters.</p>
        <div class="price"><b>From $4,500</b><span>per agent · most projects land between $4,500 and $12,000 · fixed quote before we start</span></div>
        <div class="meta"><span class="tag">2–5 weeks</span><span class="tag">30 days of tuning included</span></div>
      </div>
      <div class="offer__body">
        <div class="tiers">
          <div class="tier"><div class="tier__name">Focused agent</div><div class="tier__price">$4,500 <small>starting</small></div>
            <p class="muted small">One workflow, up to two connected tools. Live in 2–3 weeks.</p>
            {check_list(["Missed-call text-back and lead routing", "Website chat or FAQ assistant", "Review-response drafts for approval"])}</div>
          <div class="tier tier--featured"><div class="tier__name">Connected agent <span class="tag">Most chosen</span></div><div class="tier__price">$8,500 <small>starting</small></div>
            <p class="muted small">Multi-step workflows across your CRM, booking or point-of-sale system. Live in 3–5 weeks.</p>
            {check_list(["Inquiry intake, qualification and booking", "Quote and proposal drafting from your price list", "Internal knowledge assistant for staff"])}</div>
        </div>
        <div><h3>Every build includes</h3>
        {check_list([
          "Guardrails: approved answers, handoff rules, and human approval for anything sent on your behalf",
          "Testing on at least 50 real examples from your business before launch",
          "Staff walkthrough and a one-page guide for your team",
          "Everything set up in accounts you own, with full documentation",
          "30 days of monitoring and tuning after launch",
        ])}</div>
      </div>
    </article>

    <article class="offer" id="restaurants" aria-labelledby="o-rest">
      <div class="offer__head">
        <p class="label">For restaurants</p>
        <h2 id="o-rest">Restaurant Front-of-House Pack</h2>
        <p class="lead">Four services built around the moments restaurants lose customers: the unanswered catering call, the review nobody replied to, the phone that rang out at 7 PM, and the Google listing with last year's hours.</p>
        <div class="price"><b>From $1,500</b><span>setup per service, plus $150/month each to run and monitor · all four from $4,500 setup and $450/month</span></div>
        <div class="meta"><span class="tag">Live in 1–3 weeks</span><span class="tag">Works with your current phone and POS</span></div>
      </div>
      <div class="offer__body">
        <div class="tiers">
          <div class="tier"><div class="tier__name">Catering &amp; private-event inquiries</div>
            <p class="muted small">Catering and event requests never sit unanswered.</p>
            {check_list(["Instant reply to every catering call, form or message", "Collects date, headcount, budget and dietary needs", "Complete brief to your manager with a one-tap claim link", "Escalates to the owner if nobody responds in 15 minutes", "Quote drafts from your catering menu, for approval"])}</div>
          <div class="tier"><div class="tier__name">Review responses in your voice</div>
            <p class="muted small">Every review answered, in words that sound like you.</p>
            {check_list(["Drafts trained on how you actually talk to guests", "New Google and Yelp reviews checked daily", "You approve each reply; Google replies post in one tap", "Negative reviews flagged to you first, never auto-posted", "Monthly summary of what guests praise and complain about"])}</div>
          <div class="tier"><div class="tier__name">Missed-call text-back</div>
            <p class="muted small">No caller left hanging during the dinner rush.</p>
            {check_list(["A text within seconds when a call goes unanswered", "Your reservation link, hours and directions on request", "Catering and large-party requests routed to your manager", "Wording you approve, with opt-out handled automatically", "Texting registration (A2P 10DLC) handled for you"])}</div>
          <div class="tier"><div class="tier__name">Hours &amp; menu, consistent everywhere</div>
            <p class="muted small">Change it once; it's right everywhere guests look.</p>
            {check_list(["One place to update hours, holiday closures and specials", "Website and Google Business Profile update together", "Yelp and other listings updated alongside, with a checklist where a site doesn't allow automatic changes", "Weekly check that flags any listing out of sync", "Holiday-hours reminders two weeks ahead"])}</div>
        </div>
        <p class="small muted">Text messaging costs (usually a few cents per message) and Google, Yelp and phone-carrier fees are billed in your name at cost. We'll estimate them before you start.</p>
      </div>
    </article>

    <article class="offer" id="advisory" aria-labelledby="o3">
      <div class="offer__head">
        <p class="label">Improve</p>
        <h2 id="o3">Monthly Advisory &amp; Retainer</h2>
        <p class="lead">Your AI systems monitored, tuned and extended, with a senior adviser one message away. Month to month, cancel anytime.</p>
        <div class="price"><b>From $750/mo</b><span>no long-term contract · 30 days' notice to cancel</span></div>
      </div>
      <div class="offer__body">
        <div class="tiers">
          <div class="tier"><div class="tier__name">Essentials</div><div class="tier__price">$750 <small>/ month</small></div>
            {check_list(["Monitoring and fixes for your live automations", "Monthly results report against your target", "Up to 3 hours of changes each month", "Email support, next-business-day replies"])}</div>
          <div class="tier tier--featured"><div class="tier__name">Growth <span class="tag">Best value</span></div><div class="tier__price">$1,750 <small>/ month</small></div>
            {check_list(["Everything in Essentials", "One new automation every quarter", "Up to 8 hours of changes each month", "Monthly strategy call and priority support", "Quarterly team refresher on new AI tools"])}</div>
        </div>
      </div>
    </article>

    <article class="offer" id="training" aria-labelledby="o4">
      <div class="offer__head">
        <p class="label">Add-on</p>
        <h2 id="o4">Team AI Training</h2>
        <p class="lead">Practical, hands-on sessions built around the tasks your team does every day, so the tools actually get used.</p>
        <div class="price"><b>From $900</b><span>half-day session · up to 12 people · on-site or remote</span></div>
      </div>
      <div class="offer__body">
        {check_list([
          "Prompting and checking AI output for your real tasks: emails, quotes, menus, social posts",
          "What's safe to paste into AI tools and what never is",
          "A written playbook of prompts and rules your team keeps",
          "A follow-up Q&amp;A session two weeks later",
        ])}
      </div>
    </article>
  </div>
</section>

<section class="section section--tint" aria-labelledby="cmp-title">
  <div class="wrap">
    <div class="section-head"><p class="label">At a glance</p><h2 id="cmp-title">Which one is right for you?</h2></div>
    <div class="compare" role="region" aria-labelledby="cmp-title" tabindex="0">
      <table>
        <thead><tr><th scope="col"><span class="sr-only">Detail</span></th><th scope="col">Discovery Workshop</th><th scope="col">AI Agent Deployment</th><th scope="col">Monthly Advisory</th></tr></thead>
        <tbody>
          <tr><th scope="row">You walk away with</th><td>A ranked plan and one target number</td><td>A working system, live in your business</td><td>Systems that keep improving</td></tr>
          <tr><th scope="row">Time to value</th><td>3 business days</td><td>2–5 weeks</td><td>Ongoing, reported monthly</td></tr>
          <tr><th scope="row">Price</th><td>$1,500 flat</td><td>From $4,500 per agent</td><td>From $750 per month</td></tr>
          <tr><th scope="row">Commitment</th><td>One day</td><td>Fixed scope and quote</td><td>Month to month</td></tr>
          <tr><th scope="row">Restaurants</th><td>Covers front-of-house too</td><td>Or start with the Front-of-House Pack, from $1,500 per service</td><td>Includes Pack monitoring</td></tr>
          <tr><th scope="row">Start here if</th><td>You're not sure where AI fits</td><td>You know the task you want gone</td><td>You already have automations running</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{closer("Not sure which to choose? Start with the free audit.", "In 30 minutes we'll tell you which option fits, or whether you need one at all. If AI isn't the right fix for your problem, we'll say so.")}
'''

# =================================================================== USE CASES
def math_table(rows):
    body = "".join(
        f'<tr{" class=\"total\"" if i == len(rows) - 1 else ""}><td>{a}</td><td>{b}</td></tr>' for i, (a, b) in enumerate(rows))
    return f'<details class="math"><summary>Show the math and assumptions</summary><div class="table-wrap"><table><tbody>{body}</tbody></table></div></details>'

USE_CASES = f'''
<section class="page-hero aurora" aria-labelledby="uc-title">
  <div class="wrap">
    <p class="label">Use cases</p>
    <h1 id="uc-title">What AI looks like inside a small business</h1>
    <p class="lead">One system we run every day, and two worked examples showing how the same approach plays out for a restaurant and a home-services company. Each one shows the challenge, the solution and the outcome, with the math laid out so you can swap in your own numbers.</p>
    <div class="notice" role="note">{I["info"]}<p><b>How to read these.</b> The first case is our own live system. The other two are worked examples built from typical figures, not client results. Client case studies will appear here once clients give permission to share them.</p></div>
  </div>
</section>

<section class="section" style="padding-top:clamp(1.5rem,1rem + 2vw,2.5rem)">
  <div class="wrap">

    <article class="case" aria-labelledby="c1">
      <div class="case__head">
        <div><p class="label">Live system · Professional services</p><h2 id="c1">Webcattus Labs: no inquiry left waiting</h2>
          <p>A one-person studio where the founder is often on client calls or away from the desk when new inquiries arrive.</p></div>
        <span class="tag tag--live">Running now</span>
      </div>
      <div class="case__flow">
        <div class="case__col"><p class="label">Challenge</p><ul>
          <li>Inquiries landed in an inbox and waited until the next break</li>
          <li>No record of how fast each lead got a reply, or what came of it</li>
          <li>Nobody else to cover when the founder was busy</li></ul></div>
        <div class="case__col"><p class="label">AI solution</p><ul>
          <li>Lead Router captures every website form and missed call</li>
          <li>Rules sort each one (urgent, new or existing client) and alert the founder's phone with a one-tap claim link</li>
          <li>Unclaimed leads re-alert every 30 minutes; a summary arrives at 8 AM</li>
          <li>Every outcome is recorded for reporting</li></ul></div>
        <div class="case__col case__col--outcome"><p class="label">Outcome</p>
          <div class="metric"><b>Seconds</b><span>from form submission to phone alert</span></div>
          <div class="metric"><b>0</b><span>inquiries that can sit unseen: each one is re-alerted until claimed</span></div>
          <p class="small muted">Response-time and booking results will be published after 90 days of data.</p></div>
      </div>
    </article>

    <article class="case" aria-labelledby="c2">
      <div class="case__head">
        <div><p class="label">Worked example · Restaurant</p><h2 id="c2">Family restaurant: catering calls missed during the dinner rush</h2>
          <p>A 40-seat restaurant with a growing catering business. Event inquiries come in by phone, mostly between 5 and 9 PM, when nobody can answer.</p></div>
        <span class="tag">Illustrative</span>
      </div>
      <div class="case__flow">
        <div class="case__col"><p class="label">Challenge</p><ul>
          <li>About 20 catering and event calls a month go to voicemail</li>
          <li>Callbacks happen the next day, after many callers have booked elsewhere</li>
          <li>Staff spend hours a week on phone tag collecting date, headcount and budget</li></ul></div>
        <div class="case__col"><p class="label">AI solution</p><ul>
          <li>Instant text-back on every missed call</li>
          <li>An intake assistant collects event date, guest count, budget and dietary needs by text</li>
          <li>The manager gets a complete brief with a claim link; an escalation runs if nobody responds in 15 minutes</li>
          <li>Quote drafts are generated from the catering menu for the manager to approve</li></ul></div>
        <div class="case__col case__col--outcome"><p class="label">Modeled outcome</p>
          <div class="metric"><b>≈$2,600</b><span>catering revenue recovered per month</span></div>
          <div class="metric"><b>≈4 hrs</b><span>of phone tag saved each week</span></div>
          <div class="metric"><b>≈2.5 mo</b><span>to pay back setup (revenue basis)</span></div></div>
      </div>
      {math_table([
        ("Missed catering or event calls per month", "20"),
        ("Reached by instant text-back (60%)", "12"),
        ("Booked, one in three of those reached", "4"),
        ("Average catering order", "$650"),
        ("Setup: Focused agent / monthly: Essentials", "$4,500 / $750"),
        ("Recovered revenue per month (4 × $650)", "$2,600"),
      ])}
    </article>

    <article class="case" aria-labelledby="c3">
      <div class="case__head">
        <div><p class="label">Worked example · Home services</p><h2 id="c3">HVAC company: after-hours leads and office admin</h2>
          <p>A six-technician heating and air company. Evening and weekend inquiries pile up, and the office manager spends her mornings turning voicemails into dispatch notes.</p></div>
        <span class="tag">Illustrative</span>
      </div>
      <div class="case__flow">
        <div class="case__col"><p class="label">Challenge</p><ul>
          <li>About 40 inquiries a month arrive after hours; only half get a same-day reply</li>
          <li>Urgent jobs like "no heat" sit in the same voicemail box as routine questions</li>
          <li>Six hours a week of copying details between voicemail, email and the scheduling app</li></ul></div>
        <div class="case__col"><p class="label">AI solution</p><ul>
          <li>Rules spot urgent and safety words and page the on-call tech immediately</li>
          <li>Routine requests are held and assigned at 8 AM, with a backup and then the owner if nobody claims them</li>
          <li>AI turns each call and form into a clean job summary in the scheduling app</li>
          <li>Gas, smoke or sparks always go to a person with a "call now" flag</li></ul></div>
        <div class="case__col case__col--outcome"><p class="label">Modeled outcome</p>
          <div class="metric"><b>≈5</b><span>more jobs booked per month</span></div>
          <div class="metric"><b>≈$2,250</b><span>added revenue per month</span></div>
          <div class="metric"><b>≈6 hrs</b><span>of office admin saved each week</span></div></div>
      </div>
      {math_table([
        ("After-hours inquiries per month", "40"),
        ("Reached same day today (50%)", "20"),
        ("Reached same day with routing and escalation (90%)", "36"),
        ("Additional customers reached", "16"),
        ("Close rate on reached leads", "30%"),
        ("Average ticket", "$450"),
        ("Added revenue per month (≈5 jobs × $450)", "$2,250"),
      ])}
    </article>
  </div>
</section>

{closer("Want to see what this looks like with your numbers?", "Bring a rough count of your calls, inquiries and admin hours to the free audit. We'll build the same kind of estimate for your business, and tell you plainly if the numbers don't add up.")}
'''

# ======================================================================= ABOUT
ABOUT = f'''
<section class="page-hero aurora" aria-labelledby="ab-title">
  <div class="wrap">
    <p class="label">About Webcattus Labs</p>
    <h1 id="ab-title">Enterprise-grade AI skills, sized for Main Street.</h1>
    <p class="lead">Webcattus Labs is a Dallas-based AI consulting practice for small businesses. We bring the methods large companies use to automate work and make it reliable, scoped and priced for a team of 2 to 50.</p>
  </div>
</section>

<section class="section" aria-labelledby="founder-title">
  <div class="wrap founder">
    <figure class="portrait" style="margin:0" aria-label="Founder portrait placeholder">J<figcaption>Founder</figcaption></figure>
    <div class="prose">
      <p class="label">Founder</p>
      <h2 id="founder-title">Hi, I'm Jay.</h2>
      <p>I'm a data engineer. For nearly four years I built and automated production data systems at a Fortune 10 healthcare company, including the pipelines behind pharmacy benefit underwriting models, using PySpark, Databricks and Google Cloud. That work taught me what makes automation trustworthy: clear rules, careful testing, and a person in charge of anything that matters.</p>
      <p>Most small businesses never get access to that kind of engineering. They get either a pile of disconnected apps or a sales pitch full of jargon. Webcattus Labs exists to close that gap. Every system is set up properly, explained in plain English and measured against a number you care about.</p>
      <p>When you work with Webcattus Labs, you work with me directly: the person who scopes your project is the person who builds it and answers the phone afterward.</p>
      <div class="facts">
        <div class="fact"><b>Google Cloud certified</b><span>Professional Data Engineer and Professional Cloud Architect</span></div>
        <div class="fact"><b>Databricks certified</b><span>Data Engineer Professional</span></div>
        <div class="fact"><b>PMP® certified</b><span>Projects scoped, scheduled and delivered on time</span></div>
        <div class="fact"><b>Published researcher</b><span>12 peer-reviewed papers, Springer Best Paper Award (ICSSCC 2026), active peer reviewer</span></div>
        <div class="fact"><b>MS, IT Management</b><span>The University of Texas at Dallas</span></div>
        <div class="fact"><b>B.Tech, Mechanical Engineering</b><span>SRM, with research collaboration at IIT Madras</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint" aria-labelledby="phil-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Our AI philosophy</p>
      <h2 id="phil-title">Useful beats impressive.</h2>
      <p class="lead">AI is a tool, not a strategy. These beliefs shape what we recommend, and what we talk clients out of.</p>
    </div>
    <div class="grid-2">
      <div class="card"><h3>Start with the problem, not the technology</h3><p>We begin with where your week goes and where customers slip away. Sometimes the answer is AI. Sometimes it's a better form or a simple rule, and we'll tell you.</p></div>
      <div class="card"><h3>Measure everything</h3><p>Every project has one target number agreed before we start: hours saved, reply time or revenue recovered. If we can't measure it, we don't sell it.</p></div>
      <div class="card"><h3>People stay in charge</h3><p>AI drafts, sorts and reminds. People approve prices, handle complaints and make judgment calls. Anything safety-related always goes straight to a human.</p></div>
      <div class="card"><h3>No lock-in</h3><p>Everything lives in accounts you own and comes with documentation. You should keep working with us because it pays off, not because you're stuck.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="who-title">
  <div class="wrap proof">
    <div class="stack">
      <p class="label">Who we work with</p>
      <h2 id="who-title">Owner-led businesses with 2 to 50 people</h2>
      <p class="lead">Especially restaurants, home-services companies and professional practices across Dallas–Fort Worth. We work remotely anywhere in the U.S.</p>
    </div>
    <div class="stack">
      <h3>Good fit</h3>
      {check_list(["You're losing leads or hours to repetitive work", "You want results you can measure, not a science project", "You'll give us an hour a week during setup"])}
      <h3 style="margin-top:.6rem">Probably not a fit</h3>
      {check_list(["You want AI to make decisions with no human review", "You need a large in-house platform build", "You're looking for the cheapest possible chatbot"], "checks checks--x")}
    </div>
  </div>
</section>

{closer("Let's talk about your business, not about AI.", "Tell us where your week goes. We'll tell you honestly what's worth automating and what isn't.")}
'''

# ========================================================================= FAQ
def qa(q, a):
    return f'<details class="qa"><summary><span>{q}</span><span class="pm" aria-hidden="true">+</span></summary><div class="answer">{a}</div></details>'

FAQ = f'''
<section class="page-hero aurora" aria-labelledby="faq-title">
  <div class="wrap">
    <p class="label">FAQ</p>
    <h1 id="faq-title">Straight answers about AI in your business</h1>
    <p class="lead">The questions owners ask us most: about data, accuracy, cost and time. If yours isn't here, ask it on the free audit call.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(1.5rem,1rem + 2vw,2.5rem)">
  <div class="wrap faq-layout">
    <nav class="faq-nav" aria-label="FAQ topics">
      <a href="#privacy">Data &amp; privacy</a><a href="#accuracy">Accuracy &amp; control</a><a href="#timeline">Timeline &amp; cost</a><a href="#working">Working together</a>
    </nav>
    <div>
      <div class="faq-group"><h2 id="privacy">Data &amp; privacy</h2>
        {qa("What happens to my business and customer data?", "<p>It stays in your accounts. We connect only the systems a project needs, and only the fields it needs. Customer details aren't copied into spreadsheets or AI prompts unless the task requires it.</p><p>Before anything goes live, you get a one-page data map showing what's connected, where data goes and who can see it.</p>")}
        {qa("Will my data be used to train AI models?", "<p>We use business and API plans from established AI providers whose terms say your inputs aren't used to train their models. We show you those terms before you approve the build.</p>")}
        {qa("Who has access to my systems?", "<ul><li>Accounts are created in your name, not ours.</li><li>We use the narrowest access each task needs, and you can remove it anytime.</li><li>We never ask you to email passwords. Access is shared through your password manager or each tool's own invite system.</li><li>When a project ends, our access ends with it unless you're on a retainer.</li></ul>")}
        {qa("Can you work with health, legal or financial information?", "<p>Sometimes, with care. If a workflow touches regulated information, such as health records under HIPAA, we only proceed when the tools and agreements it requires are in place. We'll flag it in the audit, and we'll turn the project down rather than cut corners.</p>")}
      </div>

      <div class="faq-group"><h2 id="accuracy">Accuracy &amp; control</h2>
        {qa("What if the AI makes something up?", "<p>It's a real risk, so we design for it:</p><ul><li><b>Grounded answers:</b> assistants answer only from information you've approved, like your menu, price list and policies.</li><li><b>Narrow scope:</b> each agent does one job well instead of trying to answer everything.</li><li><b>Handoff when unsure:</b> if a question falls outside what it knows, it says so and passes it to a person.</li><li><b>Tested before launch:</b> at least 50 real examples from your business, including tricky ones.</li><li><b>Reviewed after launch:</b> conversations are logged and spot-checked every month.</li></ul>")}
        {qa("Could it say something embarrassing to a customer?", "<p>Anything sent in your name uses wording you've approved, or goes to a person for approval first. Complaints, refunds, prices and safety issues are always routed to your team.</p>")}
        {qa("Can you update Yelp and post review replies automatically?", "<p>Partly. Google Business Profile lets approved tools update hours and post review replies, so those can happen in one tap. Yelp limits what outside tools can change, so for Yelp we prepare the exact update or reply and you post it from your Yelp business account in a few seconds. A weekly check flags any listing that has drifted out of sync.</p>")}
        {qa("What isn't AI good at?", "<p>Judgment calls, sensitive conversations, anything where a mistake is expensive, and tasks where the rules change every week. We'll tell you when a task belongs with a person, or with a simple rule instead of AI.</p>")}
      </div>

      <div class="faq-group"><h2 id="timeline">Timeline &amp; cost</h2>
        {qa("How long until something is working?", "<ul><li><b>AI Readiness Audit:</b> 30 minutes, usually within a week of booking.</li><li><b>Discovery Workshop:</b> one day, with your report three business days later.</li><li><b>Focused agent:</b> live in 2–3 weeks. <b>Connected agent:</b> 3–5 weeks.</li></ul>")}
        {qa("What does it cost to run after launch?", "<p>Most builds run for tens of dollars a month in tool and usage fees, paid directly to the providers in your name. You'll see an estimate before you approve anything. Ongoing support is optional and starts at $750 a month.</p>")}
        {qa("How will I know it's working?", "<p>We agree on one target number before we start, such as reply time, hours saved or jobs booked. You get a short monthly report against that number, built from the system's own logs.</p>")}
        {qa("What if it doesn't hit the target?", "<p>We find out why and fix it. If it still isn't worth running, we'll recommend switching it off. Retainers are month to month, so you're never paying for something that doesn't pay you back.</p>")}
      </div>

      <div class="faq-group"><h2 id="working">Working together</h2>
        {qa("Do I need technical staff?", "<p>No. We handle the setup and the technical work. We need someone who knows the workflow for about an hour a week during the build, plus a short training session before launch.</p>")}
        {qa("Will AI replace my employees?", "<p>That's not how we design it. The goal is to take the repetitive parts of their jobs, like phone tag, copying details between apps and answering the same question for the tenth time, so your people spend more time on customers and the work only they can do.</p>")}
        {qa("Do you only work in Dallas–Fort Worth?", "<p>We're based in Dallas and happy to come on-site anywhere in DFW. Everything else works remotely, anywhere in the U.S.</p>")}
        {qa("Which AI tools do you use?", "<p>Whatever fits the job and the tools you already pay for. We're not resellers and don't earn commissions on software, so our recommendations aren't tied to a vendor.</p>")}
      </div>
    </div>
  </div>
</section>

{closer("Still have a question?", "Bring it to the free 30-minute audit. You'll get a straight answer, and a clear view of where AI could help your business.")}
'''

# ===================================================================== CONTACT
def opts(items):
    return "".join(f'<option>{o}</option>' for o in items)

def chips(name, items):
    return '<div class="chips">' + "".join(
        f'<label class="chip"><input type="checkbox" name="{name}" value="{_html.escape(v)}"><span>{_html.escape(v)}</span></label>' for v in items) + "</div>"

CONTACT_PAGE = f'''
<section class="page-hero aurora" aria-labelledby="ct-title">
  <div class="wrap">
    <p class="label">AI Readiness Audit</p>
    <h1 id="ct-title">Book your free AI Readiness Audit</h1>
    <p class="lead">Tell us a little about your business, then pick a time. In 30 minutes you'll learn which tasks are worth automating, roughly what each is worth, and what it would take.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(1rem,.5rem + 1.5vw,2rem)">
  <div class="wrap contact-layout">
    <div class="form-card">
      <div class="progress" aria-label="Booking progress">
        <span class="pill is-current">1 · About your business</span><span aria-hidden="true">→</span><span class="pill">2 · Pick a time</span>
      </div>

      <form id="booking-form" method="POST"
            action="https://lead-router.webcattus.workers.dev/form/webcattus?redirect=https%3A%2F%2Fwebcattuslabs.com%2Fcontact.html">
        <fieldset class="fieldset">
          <legend>About you</legend>
          <div class="fields">
            <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" autocomplete="name" required maxlength="120"></div>
            <div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="160"></div>
            <div class="field"><label for="f-company">Business name</label><input id="f-company" name="company" type="text" autocomplete="organization" required maxlength="120"></div>
            <div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="30"></div>
            <div class="field field--full"><label for="f-site">Website <span class="opt">(optional)</span></label><input id="f-site" name="site_url" type="url" inputmode="url" placeholder="https://" maxlength="200"></div>
          </div>
        </fieldset>

        <fieldset class="fieldset">
          <legend>About your business</legend>
          <div class="fields">
            <div class="field"><label for="f-industry">Industry</label>
              <select id="f-industry" name="industry" required><option value="">Choose one</option>{opts(["Restaurant or food &amp; beverage", "Home services", "Construction", "Professional services", "Health &amp; wellness", "Retail or e-commerce", "Real estate", "Other"])}</select></div>
            <div class="field"><label for="f-size">Team size</label>
              <select id="f-size" name="team_size" required><option value="">Choose one</option>{opts(["Just me", "2–10 people", "11–50 people", "51–200 people"])}</select></div>
            <div class="field field--full"><span class="field__label" id="drains-label">Where does your time go? <span class="opt">Pick any that apply</span></span>
              <div role="group" aria-labelledby="drains-label">{chips("drains", ["Missed calls & slow replies", "Catering & private events", "Online reviews", "Hours & menu listings", "Scheduling & booking", "Quotes & proposals", "Data entry & admin", "Customer questions", "Marketing & content", "Not sure yet"])}</div></div>
            <div class="field"><label for="f-budget">Budget for a first project</label>
              <select id="f-budget" name="budget"><option value="">Prefer not to say</option>{opts(["Under $2,500", "$2,500–$7,500", "$7,500–$15,000", "$15,000+", "Not sure yet"])}</select>
              <span class="hint">Helps us suggest the right starting point.</span></div>
            <div class="field"><label for="f-timeline">When do you want to start?</label>
              <select id="f-timeline" name="timeline"><option value="">Choose one</option>{opts(["As soon as possible", "Within 1–3 months", "In 3–6 months", "Just exploring"])}</select></div>
            <div class="field field--full"><label for="f-message">What would you most like to fix? <span class="opt">(optional)</span></label>
              <textarea id="f-message" name="message" maxlength="2000" placeholder="For example: we miss catering calls during dinner service, and I spend Sunday nights on invoices."></textarea></div>
          </div>
        </fieldset>

        <div class="hp" aria-hidden="true"><label for="f-hp">Leave this empty</label><input id="f-hp" name="website_hp" type="text" tabindex="-1" autocomplete="off"></div>
        <input type="hidden" name="_elapsed" value="">

        <div class="form-foot">
          <button class="btn btn--primary" type="submit">Send and pick a time {A}</button>
          <p class="small muted">We'll only use this to prepare for your call. No newsletters.</p>
        </div>
        <p class="form-status" role="alert" hidden></p>
      </form>

      <div class="booked" hidden tabindex="-1" role="status" aria-live="polite">
        <span class="mark">{I["check"]}</span>
        <h2 data-hello>Thanks. Your details are in.</h2>
        <p>Last step: choose a 30-minute slot that works for you. You'll get a calendar invite with a video link.</p>
        <a class="btn btn--primary" data-calendar hidden href="#" target="_blank" rel="noopener">Pick a time {A}</a>
        <p data-no-calendar>We'll email you two or three times within one business day. Prefer to talk sooner? Write to <b>{EMAIL}</b>.</p>
        <p class="small muted" data-preview hidden>Preview mode: nothing was sent. On webcattuslabs.com this form goes straight to Lead Router.</p>
      </div>
    </div>

    <aside class="side" aria-label="What to expect">
      <div class="card">
        <h3>What happens on the call</h3>
        <ol>
          <li>You walk us through a normal week: where time goes and where customers slip away.</li>
          <li>We point out the two or three tasks most worth automating.</li>
          <li>You get a rough estimate of hours or revenue for each, and what it would take.</li>
        </ol>
      </div>
      <div class="card">
        <h3>You'll leave with</h3>
        {check_list(["A written summary within one business day", "Honest advice, including when AI isn't the answer", "No obligation and no sales sequence"])}
      </div>
      <div class="card">
        <h3>Rather talk now?</h3>
        <p>Call or text <a href="tel:{PHONE_E164}"><b>{PHONE_DISPLAY}</b></a>, Monday to Friday, 9 AM to 6 PM Central. If we miss you, we'll call back the same day.</p>
        <div class="copyline"><code>{PHONE_DISPLAY}</code><button class="copy-btn" type="button" data-copy="{PHONE_DISPLAY}">Copy</button></div>
      </div>
      <div class="card">
        <h3>Rather email?</h3>
        <div class="copyline"><code>{EMAIL}</code><button class="copy-btn" type="button" data-copy="{EMAIL}">Copy</button></div>
        <p class="small muted">Replies within one business day, from the person who'd do the work.</p>
      </div>
    </aside>
  </div>
</section>
'''

# ================================================================== INDUSTRIES
def fixes(rows):
    head = '<div class="fix fix--head" aria-hidden="true"><span>The problem</span><span>How we fix it</span><span>Works with</span></div>'
    body = "".join(
        f'<div class="fix"><p class="fix__problem">{p}</p><p class="fix__how">{h}</p><p class="fix__tools" data-label="Works with: ">{t}</p></div>' for p, h, t in rows)
    return f'<div class="fixes" role="list">{head}{body}</div>'.replace('<div class="fix">', '<div class="fix" role="listitem">')

def industry_cta(text):
    return (f'<div class="mid-cta"><p>{text}</p><div class="cta-row">{call_button("btn btn--primary")}'
            f'<a class="btn {"btn--ghost" if PHONE_E164 else "btn--primary"}" href="{CONTACT}">Book a free consultation {A}</a></div></div>')

INDUSTRIES = f'''
<section class="page-hero aurora" aria-labelledby="in-title">
  <div class="wrap">
    <p class="label">Industries · Problems we fix</p>
    <h1 id="in-title">We fix the bottlenecks that slow your business down.</h1>
    <p class="lead">Missed calls, forgotten follow-ups, paperwork after hours, numbers you never see. Here's what we fix for restaurants, home-services companies and construction firms. Call us for a free consultation and we'll tell you which fixes will make the biggest difference for you.</p>
    <nav class="jump" aria-label="Jump to an industry">
      <a href="#restaurants">{I["plate"]}Restaurants</a><a href="#home-services">{I["thermo"]}HVAC &amp; home services</a><a href="#construction">{I["hardhat"]}Construction</a>
    </nav>
  </div>
</section>

<section class="section" style="padding-top:clamp(1.5rem,1rem + 2vw,2.5rem)">
  <div class="wrap">

    <div class="industry" id="restaurants">
      <div class="industry__head"><div class="stack"><p class="label">Restaurants</p><h2>More bookings, fewer headaches, better margins.</h2>
        <p class="lead">For restaurants, cafés, bakeries and caterers. The busiest hours are when you lose the most, and that's exactly where these fixes work.</p></div>
        <a class="btn btn--ghost" href="services.html#restaurants">Restaurant pricing {A}</a></div>
      {fixes([
        ("Catering and event inquiries go unanswered", "Every catering call, form or message gets an instant reply that collects date, headcount and budget, then goes to your manager as a complete brief.", "Phone, website, email"),
        ("Reviews sit without a reply", "Replies drafted in your voice for your approval. Thank-yous go out fast; complaints come to you first.", "Google, Yelp"),
        ("Calls ring out during the dinner rush", "Callers get a friendly text within seconds with your reservation link, hours or a way to leave a request.", "Your current phone number"),
        ("Hours and menus don't match across the web", "Update once; your website and Google listing change together, Yelp follows, and a weekly check flags mismatches.", "Google, Yelp, your website"),
        ("No-shows leave empty tables", "Confirmation and reminder texts, and cancellations offered to your waitlist automatically.", "Reservation system or forms"),
        ("Last-minute staff call-outs", "Open shifts texted to qualified staff; the first yes fills it, with manager approval.", "7shifts, Homebase, staff list"),
        ("Food costs creep up unnoticed", "Supplier invoices read automatically, price jumps flagged, and a weekly food-cost report.", "Sysco, US Foods invoices"),
        ("You don't know how yesterday went", "A morning text with sales, labor percentage, comps, voids and top sellers.", "Toast, Square, Clover"),
        ("Delivery-app payouts don't add up", "Payouts matched against orders, with missing refunds flagged so you can dispute them.", "DoorDash, Uber Eats"),
        ("Regulars quietly stop coming", "Win-back and birthday messages to guests who've opted in.", "POS customer data"),
      ])}
      <p class="caution">{I["info"]}<span>Allergen questions always go to your staff. Any assistant we build answers only from your approved allergen list and tells guests to confirm with their server.</span></p>
      {industry_cta("Running a restaurant is hard enough. Let us take some of it off your plate.")}
    </div>

    <div class="industry" id="home-services">
      <div class="industry__head"><div class="stack"><p class="label">HVAC &amp; home services</p><h2>Book more jobs and spend less time on paperwork.</h2>
        <p class="lead">For HVAC, plumbing, electrical, roofing and other field-service businesses. Speed wins jobs, and paperwork eats margins.</p></div></div>
      {fixes([
        ("Leads missed after hours or during jobs", "Every call and form logged, sorted, and sent to the right person's phone, with escalation until someone claims it. Gas, smoke or no-heat calls go straight to the on-call tech.", "Your phone, website, Slack or text"),
        ("Estimates that never get followed up", "Unsold estimates chased automatically at day 2, 5 and 10; hot replies go to the salesperson.", "ServiceTitan, Housecall Pro, Jobber"),
        ("Maintenance agreements lapse", "Renewal reminders and seasonal tune-up campaigns that book straight into your calendar.", "Customer list, scheduling tool"),
        ("Techs hate paperwork", "A 30-second voice note after each job becomes clean job notes, an invoice draft and a customer summary.", "Phone app, job software"),
        ("Too few online reviews", "A review request two hours after each completed job; unhappy replies go to the manager instead of Google.", "Google, job software"),
        ("Same questions in the field", "Techs look up error codes and specs from the manuals you load in.", "Manufacturer manuals"),
        ("No clear view of the numbers", "A weekly report on close rate, average ticket, callbacks and tech performance.", "Your job software"),
      ])}
      {industry_cta("Your techs should be fixing systems, not typing notes. Let's talk about it.")}
    </div>

    <div class="industry" id="construction">
      <div class="industry__head"><div class="stack"><p class="label">Construction</p><h2>Less chasing, cleaner records, faster payment.</h2>
        <p class="lead">For general contractors, remodelers and specialty subcontractors. Documentation and follow-up decide whether a job makes money.</p></div></div>
      {fixes([
        ("Daily logs never get written", "Site photos and voice notes become a daily log and weekly progress report automatically.", "Phone, Google Drive, Buildertrend, Procore"),
        ("Change orders slip through", "Field notes turn into a change-order draft sent for e-signature the same day.", "Your templates, e-signature"),
        ("Subcontractor insurance expires unnoticed", "Each sub's certificate of insurance tracked, with reminders before expiry and a payment hold flag.", "Spreadsheet or email"),
        ("Homeowners keep calling for updates", "A weekly update drafted from logs and photos, approved by you before it's sent.", "Your daily logs"),
        ("Bid invitations pile up", "Incoming bid invites summarized with scope, due date and a go/no-go checklist.", "Email"),
        ("Getting paid takes too long", "Overdue invoices, pay applications and lien waivers chased on a schedule.", "QuickBooks"),
        ("Subs show up late or not at all", "Confirmation and reminder texts, and a heads-up to the project manager when someone's running late.", "Your schedule"),
      ])}
      {industry_cta("Spend your time building, not chasing paperwork. Call us and we'll show you how.")}
    </div>
  </div>
</section>

{closer("Whatever's slowing you down, let's fix it.", "Call us or book a free 30-minute consultation. Tell us where your week goes, and we'll show you what to fix first, how we'd do it, and what it's worth. If AI isn't the right answer, we'll tell you that too.")}
'''

PAGES = [
  {"path": "index.html", "title": "Webcattus Labs", "body": HOME,
   "desc": "AI consulting for small businesses in Dallas–Fort Worth. We automate follow-ups, admin and customer questions, with a measurable target in hours saved or revenue recovered."},
  {"path": "services.html", "title": "Services & Pricing · Webcattus Labs", "body": SERVICES,
   "desc": "AI Discovery Workshop, custom AI agent deployment and monthly advisory for small businesses. Clear deliverables and fixed prices."},
  {"path": "industries.html", "title": "Industries · Webcattus Labs", "body": INDUSTRIES,
   "desc": "The bottlenecks we fix for restaurants, HVAC and home-services companies, and construction firms. Call for a free consultation."},
  {"path": "use-cases.html", "title": "Use Cases · Webcattus Labs", "body": USE_CASES,
   "desc": "How AI follow-up and automation work inside small businesses: challenge, solution and outcome, with the math shown."},
  {"path": "about.html", "title": "About · Webcattus Labs", "body": ABOUT,
   "desc": "Webcattus Labs brings enterprise data-engineering skills to small businesses. Meet the founder and our approach to practical, responsible AI."},
  {"path": "faq.html", "title": "FAQ · Webcattus Labs", "body": FAQ,
   "desc": "Answers about AI for small business: data privacy, security, accuracy, timelines and cost."},
  {"path": "contact.html", "title": "Book an AI Readiness Audit · Webcattus Labs", "body": CONTACT_PAGE,
   "desc": "Book a free 30-minute AI Readiness Audit with Webcattus Labs."},
]
