"""Contenido en español del sitio de Webcattus Labs. Edite el texto aquí y ejecute build.py.
Se usa "usted" en todo el sitio. Los valores que llegan a Lead Router (opciones del formulario)
se envían en inglés para que las alertas en Slack se lean igual que las del sitio en inglés."""
import html as _html
from build import I, CONTACT, EMAIL, PHONE_E164, PHONE_DISPLAY, closer, call_button

A = I["arrow"]

def fix_bullets(items):
    return "<ul>" + "".join(f'<li>{I["check"]}<span>{t}</span></li>' for t in items) + "</ul>"

def check_list(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f'<li>{I["check"]}<span>{t}</span></li>' for t in items) + "</ul>"

def consult_cta(text):
    second = "btn--ghost" if PHONE_E164 else "btn--primary"
    return (f'<div class="mid-cta"><p>{text}</p><div class="cta-row">{call_button("btn btn--primary")}'
            f'<a class="btn {second}" href="{CONTACT}">Reserve una consulta gratuita {A}</a></div></div>')

# ======================================================================= INICIO
HOME = f'''
<section class="hero aurora" aria-labelledby="hero-title">
  <div class="grid-lines" aria-hidden="true"></div>
  <div class="wrap hero__grid">
    <div class="hero__copy">
      <p class="label rise">Consultoría de IA para pequeños negocios · Dallas–Fort Worth</p>
      <h1 id="hero-title" class="rise rise-2">IA que le devuelve sus <em>horas</em> y los clientes que se le escapan.</h1>
      <p class="lead rise rise-3">Webcattus Labs ayuda a dueños de pequeños negocios a automatizar el seguimiento, el papeleo y las preguntas de clientes que les consumen la semana. Antes de construir nada, acordamos una meta en horas ahorradas o ingresos recuperados, y le reportamos los resultados cada mes.</p>
      <div class="cta-row rise rise-4">
        <a class="btn btn--primary" href="{CONTACT}">Reserve su diagnóstico de IA {A}</a>
        <a class="btn btn--ghost" href="#how">Vea cómo funciona</a>
      </div>
      <p class="cta-note rise rise-4"><span>Llamada gratuita de 30 minutos</span><span>Sin preparación</span><span>Respuestas claras, sin tecnicismos</span></p>
      <p class="small muted rise rise-4">¿Prefiere hablar ahora? Llame al <a href="tel:{PHONE_E164}"><b>{PHONE_DISPLAY}</b></a></p>
    </div>

    <figure class="console rise rise-5" aria-label="Ilustración: cómo un sistema de seguimiento con IA atiende una llamada perdida">
      <div class="console__bar">
        <span class="console__title">Llamada perdida → trabajo reservado</span>
        <span class="tag">Ejemplo</span>
      </div>
      <ol class="timeline">
        <li><time>7:42 p. m.</time><span class="dot">{I["phone"]}</span><div><strong>Llamada perdida en plena hora de la cena</strong><span>(214) •••-0142 · cliente nuevo</span></div></li>
        <li><time>7:42 p. m.</time><span class="dot dot--accent">{I["msg"]}</span><div><strong>Mensaje de texto enviado al cliente</strong><span>"Disculpe que no pudimos contestar. ¿En qué le ayudamos?"</span></div></li>
        <li><time>7:43 p. m.</time><span class="dot dot--accent">{I["bell"]}</span><div><strong>Enviado a María, de guardia esta noche</strong><span>El cliente respondió: "Banquete para 40 el sábado"</span></div></li>
        <li><time>7:47 p. m.</time><span class="dot dot--good">{I["user"]}</span><div><strong>María lo tomó y devolvió la llamada</strong><span>No se molestó a nadie más</span></div></li>
        <li><time>7:58 p. m.</time><span class="dot dot--good">{I["check"]}</span><div><strong>Reservado: banquete del sábado, 40 invitados</strong><span>Registrado con su resultado para el reporte mensual</span></div></li>
      </ol>
      <figcaption class="console__foot"><span>Primera respuesta en <b>menos de 1 min</b></span><span>Intervención del dueño <b>ninguna</b></span></figcaption>
    </figure>
  </div>
</section>

<section class="creds" aria-label="Credenciales del fundador">
  <div class="wrap">
    <p class="creds__label">Las credenciales detrás de cada proyecto</p>
    <ul>
      <li>{I["badge"]}Google Cloud Professional Data Engineer</li>
      <li>{I["badge"]}Google Cloud Professional Cloud Architect</li>
      <li>{I["badge"]}Databricks Data Engineer Professional</li>
      <li>{I["badge"]}Certificación PMP®</li>
      <li>{I["book"]}12 publicaciones arbitradas</li>
      <li>{I["award"]}Premio Springer al Mejor Artículo, 2026</li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="pain-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">El problema</p>
      <h2 id="pain-title">Los pequeños negocios no pierden ante los más grandes. Pierden ante los más rápidos.</h2>
      <p class="lead">La mayoría de los pequeños negocios tienen las mismas tres fugas. Ninguna requiere contratar a alguien más. Todas se pueden resolver con IA bien configurada.</p>
    </div>
    <div class="pains">
      <div class="pain"><p class="stat">Gana quien responde primero.</p><p>El cliente que no logra comunicarse con usted llama al siguiente negocio de la lista. Las llamadas perdidas en horas pico y los formularios que esperan hasta el día siguiente son ventas que se van.</p></div>
      <div class="pain"><p class="stat">El turno del papeleo a las 9 p. m.</p><p>Cotizaciones, seguimientos, agenda, captura de datos y las mismas cinco preguntas de siempre. El dueño termina haciéndolo después de cerrar, todas las noches.</p></div>
      <div class="pain"><p class="stat">Herramientas que no se hablan.</p><p>El teléfono, el correo, el sistema de reservas y la hoja de cálculo tienen cada uno una parte de la información. Las cosas se pierden entre una y otra.</p></div>
    </div>
  </div>
</section>

<section class="section section--tint" aria-labelledby="services-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Lo que hacemos</p>
      <h2 id="services-title">Cuatro formas de poner la IA a trabajar para usted</h2>
      <p class="lead">Empiece con un plan, automatice el trabajo que más importa y asegúrese de que su equipo realmente lo use.</p>
    </div>
    <div class="grid-4">
      <a class="card card-link" href="services.html#workshop">
        <span class="icon">{I["compass"]}</span><h3>Estrategia de IA</h3>
        <p>Identificamos las dos o tres tareas donde la IA rinde más rápido, con una estimación de costo y retorno para cada una.</p>
        <p class="result">Resultado típico: <b>un plan de 90 días listo para ejecutar</b></p>
        <span class="more">Taller de descubrimiento {A}</span>
      </a>
      <a class="card card-link" href="services.html#agents">
        <span class="icon">{I["flow"]}</span><h3>Automatización de procesos</h3>
        <p>El seguimiento de clientes, la agenda, el registro de solicitudes y los reportes funcionan solos y pasan a una persona cuando hace falta.</p>
        <p class="result">Meta típica: <b>recuperar de 5 a 10 horas por semana</b></p>
        <span class="more">Agentes de IA a la medida {A}</span>
      </a>
      <a class="card card-link" href="services.html#agents">
        <span class="icon">{I["chat"]}</span><h3>Asistentes de IA a la medida</h3>
        <p>Asistentes entrenados con sus menús, precios y políticas que responden con precisión a clientes y empleados, a cualquier hora.</p>
        <p class="result">Meta típica: <b>respuestas en minutos, no en horas</b></p>
        <span class="more">Agentes de IA a la medida {A}</span>
      </a>
      <a class="card card-link" href="services.html#training">
        <span class="icon">{I["users"]}</span><h3>Capacitación en IA</h3>
        <p>Sesiones prácticas basadas en las tareas reales de su equipo, para que las herramientas de IA se usen de forma segura todos los días.</p>
        <p class="result">Resultado típico: <b>una guía compartida que su equipo conserva</b></p>
        <span class="more">Capacitación en IA {A}</span>
      </a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ind-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Problemas que resolvemos</p>
      <h2 id="ind-title">Si algo frena su negocio, probablemente lo podemos resolver.</h2>
      <p class="lead">Estos son los cuellos de botella que más vemos en restaurantes, empresas de servicios para el hogar y constructoras. Configuramos la solución, capacitamos a su equipo y nos aseguramos de que siga funcionando.</p>
    </div>
    <div class="ind-cols">
      <div class="ind-col">
        <h3><span class="icon">{I["plate"]}</span>Restaurantes</h3>
        {fix_bullets(["Solicitudes de banquetes y eventos privados que nunca se quedan sin respuesta", "Respuestas a reseñas redactadas con su propia voz", "Mensaje de texto automático cuando no alcanza a contestar en la hora pico", "Horarios y menú siempre iguales en Google, Yelp y su sitio web", "Recordatorios contra ausencias, cobertura de turnos y un resumen de ventas cada mañana"])}
        <a class="more" href="industries.html#restaurants">Todas las soluciones para restaurantes {A}</a>
      </div>
      <div class="ind-col">
        <h3><span class="icon">{I["thermo"]}</span>HVAC y servicios para el hogar</h3>
        {fix_bullets(["Seguimiento automático de cotizaciones sin cerrar", "Llamadas fuera de horario agendadas o enviadas al técnico de guardia", "Contratos de mantenimiento renovados antes de que venzan", "Notas de voz convertidas en reportes de trabajo y facturas", "Solicitud de reseñas después de cada trabajo terminado"])}
        <a class="more" href="industries.html#home-services">Todas las soluciones para servicios {A}</a>
      </div>
      <div class="ind-col">
        <h3><span class="icon">{I["hardhat"]}</span>Construcción</h3>
        {fix_bullets(["Bitácoras diarias y reportes de avance a partir de fotos y notas de voz", "Órdenes de cambio redactadas y enviadas a firma el mismo día", "Certificados de seguro de subcontratistas vigilados antes de que venzan", "Actualizaciones semanales para el cliente sin tantas llamadas", "Cobro de facturas vencidas y renuncias de gravamen en tiempo"])}
        <a class="more" href="industries.html#construction">Todas las soluciones para construcción {A}</a>
      </div>
    </div>
    {consult_cta("¿No ve su problema? Cuéntenos. La mayor parte de lo que construimos es a la medida.")}
  </div>
</section>

<section class="section section--tint" aria-labelledby="calc-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Haga las cuentas</p>
      <h2 id="calc-title">¿Cuánto le cuesta responder tarde?</h2>
      <p class="lead">Mueva los controles según su negocio. El cálculo se hace en su navegador y no se envía nada.</p>
    </div>
    <div class="calc" id="calc">
      <div class="calc__inputs">
        <div class="calc__field">
          <div class="calc__row"><label for="calc-missed">Solicitudes perdidas o atendidas tarde</label><output id="out-missed" for="calc-missed">8 / semana</output></div>
          <input id="calc-missed" type="range" min="1" max="40" step="1" value="8">
          <p class="calc__hint">Llamadas perdidas, mensajes de voz y formularios que esperaron más de una hora.</p>
        </div>
        <div class="calc__field">
          <div class="calc__row"><label for="calc-rate">Porcentaje que ganaría respondiendo rápido</label><output id="out-rate" for="calc-rate">25%</output></div>
          <input id="calc-rate" type="range" min="5" max="60" step="5" value="25">
          <p class="calc__hint">Sea conservador. Uno de cada cuatro es un buen punto de partida.</p>
        </div>
        <div class="calc__field">
          <div class="calc__row"><label for="calc-value">Valor promedio de una venta o trabajo</label><output id="out-value" for="calc-value">$400</output></div>
          <input id="calc-value" type="range" min="50" max="5000" step="50" value="400">
          <p class="calc__hint">Un pedido, servicio o primera factura típica.</p>
        </div>
      </div>
      <div class="calc__result" aria-live="polite">
        <p class="label">Ingresos en riesgo</p>
        <p class="calc__big" id="out-month">$3,467</p>
        <p class="calc__year">al mes, o cerca de <b id="out-year">$41,600</b> al año</p>
        <p class="small">Es una estimación con sus datos, no una promesa. En el diagnóstico la comparamos con sus llamadas y solicitudes reales.</p>
        <a class="btn btn--light" href="{CONTACT}">Revisar mis números reales {A}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="how" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Cómo funciona</p>
      <h2 id="how-title">De la primera llamada a resultados medibles en un mes, aproximadamente</h2>
    </div>
    <ol class="steps es-steps">
      <li class="step"><h3>Encontrar la fuga</h3><p class="when">Diagnóstico gratuito y después la semana 1</p>
        <p>Un diagnóstico de IA de 30 minutos y, si lo desea, un taller de un día. Identificamos dónde se pierden tiempo y clientes, y acordamos una sola meta medible.</p></li>
      <li class="step"><h3>Construir con salvaguardas</h3><p class="when">Semanas 2 a 4</p>
        <p>Configuramos la automatización dentro de las herramientas que ya usa, la probamos con ejemplos reales de su negocio y capacitamos a su equipo antes de lanzarla.</p></li>
      <li class="step"><h3>Medir y mejorar</h3><p class="when">Cada mes</p>
        <p>Un reporte breve de horas ahorradas, respuestas enviadas y trabajos reservados frente a la meta. Ajustamos lo que funciona y apagamos lo que no.</p></li>
    </ol>
  </div>
</section>

<section class="section section--tint" aria-labelledby="proof-title">
  <div class="wrap proof">
    <div class="stack">
      <p class="label">Pruebas, no promesas</p>
      <h2 id="proof-title">Usamos en nuestro negocio lo mismo que vendemos.</h2>
      <p class="lead">Cada solicitud que recibe Webcattus Labs, incluido el formulario de este sitio, pasa por Lead Router, el mismo sistema de seguimiento que instalamos para nuestros clientes. Nada se queda esperando en una bandeja de entrada.</p>
      {check_list([
        "Cada llamada y formulario se registra, se clasifica y llega al teléfono de la persona indicada",
        "Si nadie lo toma, se escala automáticamente hasta que alguien lo atiende",
        "Se registra el resultado de cada solicitud, así el reporte mensual muestra trabajo cerrado, no solo actividad",
        "Las solicitudes delicadas o poco claras siempre van a una persona, nunca solo a la IA",
      ])}
      <div class="cta-row"><a class="btn btn--ghost" href="use-cases.html">Ver los casos de uso {A}</a></div>
    </div>
    <div class="specs" aria-label="Datos de Lead Router">
      <div class="spec"><b>Segundos</b><span>desde una nueva solicitud hasta la alerta en su teléfono</span></div>
      <div class="spec"><b>10 min</b><span>de espera predeterminada antes de escalar una solicitud sin atender</span></div>
      <div class="spec"><b>8:00 a. m.</b><span>resumen diario de cada solicitud y su resultado</span></div>
      <div class="spec"><b>48</b><span>pruebas automáticas antes de cada cambio en producción</span></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="trust-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Responsable desde el diseño</p>
      <h2 id="trust-title">IA en la que puede confiar con sus clientes</h2>
      <p class="lead">La pregunta no es si la IA puede hacer la tarea, sino si puede confiarle su reputación. Estas reglas vienen con cada proyecto.</p>
    </div>
    <div class="principles">
      <div class="principle"><span class="icon">{I["hand"]}</span><h3>Una persona aprueba lo importante</h3><p>Precios, promesas, quejas y todo lo relacionado con seguridad pasan por una persona. La IA redacta; su equipo decide.</p></div>
      <div class="principle"><span class="icon">{I["lock"]}</span><h3>Sus datos son suyos</h3><p>Usamos planes empresariales de IA que no se entrenan con sus datos, y solo conectamos lo que el trabajo necesita.</p></div>
      <div class="principle"><span class="icon">{I["info"]}</span><h3>Sabe cuándo no sabe</h3><p>Los asistentes responden con la información que usted aprobó. Cuando tienen dudas, pasan la conversación a una persona en lugar de adivinar.</p></div>
      <div class="principle"><span class="icon">{I["key"]}</span><h3>Todo queda a su nombre</h3><p>Las cuentas, los datos y las configuraciones son suyos. Si dejamos de trabajar juntos, todo sigue funcionando sin nosotros.</p></div>
    </div>
    <p class="muted small" style="margin-top:2rem">Funciona con las herramientas que ya usa, como Google Workspace, Microsoft 365, Slack, Teams, Square, Shopify, QuickBooks y HubSpot. Los mensajes para sus clientes pueden enviarse en inglés, en español o en ambos.</p>
  </div>
</section>

{closer()}
'''

# =================================================================== SERVICIOS
SERVICES = f'''
<section class="page-hero aurora" aria-labelledby="svc-title">
  <div class="wrap">
    <p class="label">Servicios y precios</p>
    <h1 id="svc-title">Alcance claro. Precios fijos. Resultados medibles.</h1>
    <p class="lead">Todo comienza con un diagnóstico de IA gratuito. A partir de ahí, la mayoría de nuestros clientes sigue el mismo camino: planear, construir y mejorar mes a mes. Puede detenerse después de cualquier paso.</p>
    <div class="cta-row"><a class="btn btn--primary" href="{CONTACT}">Reserve su diagnóstico de IA {A}</a><span class="muted small">Gratis · 30 minutos · Recibe un resumen por escrito</span></div>
  </div>
</section>

<section class="section" style="padding-top:clamp(2rem,1.5rem + 2vw,3rem)">
  <div class="wrap">

    <article class="offer" id="workshop" aria-labelledby="o1">
      <div class="offer__head">
        <p class="label">Planear</p>
        <h2 id="o1">Taller de descubrimiento de IA (1 día)</h2>
        <p class="lead">Un día de trabajo enfocado con usted y su equipo clave para encontrar dónde la IA ahorra más tiempo y dinero, y qué se necesita para lograrlo.</p>
        <div class="price"><b>$1,500</b><span>tarifa fija · presencial en DFW o a distancia · se acredita a su primer proyecto si lo inicia dentro de 60 días</span></div>
        <div class="meta"><span class="tag">1 día + reporte en 3 días hábiles</span><span class="tag">Hasta 6 participantes</span></div>
      </div>
      <div class="offer__body">
        <div><h3>Lo que recibe</h3>
        {check_list([
          "Un mapa de sus 10 procesos que más tiempo consumen, con las horas semanales de cada uno",
          "Una lista de oportunidades ordenada por retorno: horas ahorradas, impacto en ingresos, costo de implementación y de operación",
          "Recomendaciones de herramientas compatibles con lo que ya usa, con ventajas y desventajas honestas",
          "Un plan de 90 días con una meta acordada desde el inicio",
          "Una revisión de riesgos y privacidad de datos para cada recomendación",
          "Un reporte escrito y la grabación, entregados en 3 días hábiles",
        ])}</div>
        <div><h3>Ideal para</h3><p class="muted">Dueños que saben que la IA podría ayudarles pero no saben por dónde empezar, o que ya probaron herramientas que nunca funcionaron.</p></div>
      </div>
    </article>

    <article class="offer" id="agents" aria-labelledby="o2">
      <div class="offer__head">
        <p class="label">Construir</p>
        <h2 id="o2">Implementación de agentes de IA a la medida</h2>
        <p class="lead">Construimos, conectamos y lanzamos un agente de IA que se encarga de un proceso de principio a fin, con una persona al mando en cada paso importante.</p>
        <div class="price"><b>Desde $4,500</b><span>por agente · la mayoría de los proyectos cuesta entre $4,500 y $12,000 · cotización fija antes de empezar</span></div>
        <div class="meta"><span class="tag">2 a 5 semanas</span><span class="tag">Incluye 30 días de ajustes</span></div>
      </div>
      <div class="offer__body">
        <div class="tiers">
          <div class="tier"><div class="tier__name">Agente enfocado</div><div class="tier__price">$4,500 <small>desde</small></div>
            <p class="muted small">Un proceso y hasta dos herramientas conectadas. Listo en 2 a 3 semanas.</p>
            {check_list(["Mensaje automático por llamada perdida y distribución de solicitudes", "Chat o asistente de preguntas frecuentes en su sitio", "Borradores de respuestas a reseñas para su aprobación"])}</div>
          <div class="tier tier--featured"><div class="tier__name">Agente conectado <span class="tag">El más elegido</span></div><div class="tier__price">$8,500 <small>desde</small></div>
            <p class="muted small">Procesos de varios pasos con su CRM, sistema de reservas o punto de venta. Listo en 3 a 5 semanas.</p>
            {check_list(["Registro, calificación y agenda de solicitudes", "Cotizaciones y propuestas a partir de su lista de precios", "Asistente interno de conocimiento para su personal"])}</div>
        </div>
        <div><h3>Cada proyecto incluye</h3>
        {check_list([
          "Salvaguardas: respuestas aprobadas, reglas para pasar a una persona y aprobación humana de todo lo que se envía en su nombre",
          "Pruebas con al menos 50 ejemplos reales de su negocio antes del lanzamiento",
          "Capacitación al personal y una guía de una página para su equipo",
          "Todo configurado en cuentas a su nombre, con documentación completa",
          "30 días de monitoreo y ajustes después del lanzamiento",
        ])}</div>
      </div>
    </article>

    <article class="offer" id="restaurants" aria-labelledby="o-rest">
      <div class="offer__head">
        <p class="label">Para restaurantes</p>
        <h2 id="o-rest">Paquete de atención al cliente para restaurantes</h2>
        <p class="lead">Cuatro servicios pensados para los momentos en que un restaurante pierde clientes: la llamada de banquete sin respuesta, la reseña sin contestar, el teléfono que nadie atendió a las 7 p. m. y el perfil de Google con el horario del año pasado.</p>
        <div class="price"><b>Desde $1,500</b><span>de implementación por servicio, más $150 al mes cada uno por operación y monitoreo · los cuatro desde $4,500 de implementación y $450 al mes</span></div>
        <div class="meta"><span class="tag">Listo en 1 a 3 semanas</span><span class="tag">Funciona con su teléfono y punto de venta actuales</span></div>
      </div>
      <div class="offer__body">
        <div class="tiers">
          <div class="tier"><div class="tier__name">Solicitudes de banquetes y eventos privados</div>
            <p class="muted small">Ninguna solicitud de banquete o evento se queda sin respuesta.</p>
            {check_list(["Respuesta inmediata a cada llamada, formulario o mensaje de banquete", "Recopila fecha, número de invitados, presupuesto y restricciones alimentarias", "Resumen completo para su gerente con un enlace para tomarlo con un toque", "Se escala al dueño si nadie responde en 15 minutos", "Borradores de cotización basados en su menú de banquetes, para su aprobación"])}</div>
          <div class="tier"><div class="tier__name">Respuestas a reseñas con su voz</div>
            <p class="muted small">Cada reseña contestada, con palabras que suenan a usted.</p>
            {check_list(["Borradores basados en cómo usted les habla a sus clientes", "Revisión diaria de nuevas reseñas en Google y Yelp", "Usted aprueba cada respuesta; en Google se publica con un toque", "Las reseñas negativas le llegan primero a usted, nunca se publican solas", "Resumen mensual de lo que sus clientes elogian y critican"])}</div>
          <div class="tier"><div class="tier__name">Mensaje automático por llamada perdida</div>
            <p class="muted small">Ningún cliente se queda esperando en la hora de la cena.</p>
            {check_list(["Un mensaje de texto en segundos cuando no se contesta una llamada", "Su enlace de reservaciones, horario y ubicación si el cliente los pide", "Banquetes y grupos grandes enviados a su gerente", "Textos aprobados por usted, con opción de darse de baja", "Nos encargamos del registro para mensajes comerciales (A2P 10DLC)"])}</div>
          <div class="tier"><div class="tier__name">Horario y menú, iguales en todas partes</div>
            <p class="muted small">Cámbielo una vez y quedará correcto donde sus clientes lo busquen.</p>
            {check_list(["Un solo lugar para actualizar horarios, cierres por días festivos y especiales", "Su sitio web y su perfil de Google se actualizan al mismo tiempo", "Yelp y otros directorios se actualizan también, con una lista de pasos donde no se permiten cambios automáticos", "Revisión semanal que avisa si algún perfil no coincide", "Recordatorio de horarios festivos dos semanas antes"])}</div>
        </div>
        <p class="small muted">El costo de los mensajes de texto (normalmente unos centavos por mensaje) y las tarifas de Google, Yelp y la compañía telefónica se cobran a su nombre al costo. Le daremos una estimación antes de empezar. Los mensajes pueden enviarse en inglés, en español o en ambos.</p>
      </div>
    </article>

    <article class="offer" id="advisory" aria-labelledby="o3">
      <div class="offer__head">
        <p class="label">Mejorar</p>
        <h2 id="o3">Asesoría mensual y soporte continuo</h2>
        <p class="lead">Sus sistemas de IA monitoreados, ajustados y ampliados, con un asesor experto a un mensaje de distancia. Mes a mes, cancele cuando quiera.</p>
        <div class="price"><b>Desde $750 al mes</b><span>sin contrato a largo plazo · aviso de 30 días para cancelar</span></div>
      </div>
      <div class="offer__body">
        <div class="tiers">
          <div class="tier"><div class="tier__name">Esencial</div><div class="tier__price">$750 <small>/ mes</small></div>
            {check_list(["Monitoreo y correcciones de sus automatizaciones activas", "Reporte mensual de resultados frente a su meta", "Hasta 3 horas de cambios al mes", "Soporte por correo con respuesta al siguiente día hábil"])}</div>
          <div class="tier tier--featured"><div class="tier__name">Crecimiento <span class="tag">Mejor valor</span></div><div class="tier__price">$1,750 <small>/ mes</small></div>
            {check_list(["Todo lo del plan Esencial", "Una automatización nueva cada trimestre", "Hasta 8 horas de cambios al mes", "Llamada mensual de estrategia y soporte prioritario", "Actualización trimestral para su equipo sobre nuevas herramientas de IA"])}</div>
        </div>
      </div>
    </article>

    <article class="offer" id="training" aria-labelledby="o4">
      <div class="offer__head">
        <p class="label">Complemento</p>
        <h2 id="o4">Capacitación en IA para su equipo</h2>
        <p class="lead">Sesiones prácticas basadas en las tareas diarias de su equipo, para que las herramientas realmente se usen.</p>
        <div class="price"><b>Desde $900</b><span>sesión de medio día · hasta 12 personas · presencial o a distancia</span></div>
      </div>
      <div class="offer__body">
        {check_list([
          "Cómo pedirle cosas a la IA y revisar sus resultados en sus tareas reales: correos, cotizaciones, menús, publicaciones",
          "Qué es seguro pegar en una herramienta de IA y qué nunca",
          "Una guía escrita de instrucciones y reglas que su equipo conserva",
          "Una sesión de preguntas y respuestas dos semanas después",
        ])}
      </div>
    </article>
  </div>
</section>

<section class="section section--tint" aria-labelledby="cmp-title">
  <div class="wrap">
    <div class="section-head"><p class="label">Comparación rápida</p><h2 id="cmp-title">¿Cuál es el adecuado para usted?</h2></div>
    <div class="compare" role="region" aria-labelledby="cmp-title" tabindex="0">
      <table>
        <thead><tr><th scope="col"><span class="sr-only">Detalle</span></th><th scope="col">Taller de descubrimiento</th><th scope="col">Agente de IA</th><th scope="col">Asesoría mensual</th></tr></thead>
        <tbody>
          <tr><th scope="row">Lo que obtiene</th><td>Un plan priorizado y una meta medible</td><td>Un sistema funcionando en su negocio</td><td>Sistemas que mejoran cada mes</td></tr>
          <tr><th scope="row">Tiempo para ver valor</th><td>3 días hábiles</td><td>2 a 5 semanas</td><td>Continuo, con reporte mensual</td></tr>
          <tr><th scope="row">Precio</th><td>$1,500 fijo</td><td>Desde $4,500 por agente</td><td>Desde $750 al mes</td></tr>
          <tr><th scope="row">Compromiso</th><td>Un día</td><td>Alcance y cotización fijos</td><td>Mes a mes</td></tr>
          <tr><th scope="row">Restaurantes</th><td>Incluye la atención al cliente</td><td>O empiece con el paquete para restaurantes, desde $1,500 por servicio</td><td>Incluye el monitoreo del paquete</td></tr>
          <tr><th scope="row">Empiece aquí si</th><td>No sabe dónde encaja la IA</td><td>Ya sabe qué tarea quiere eliminar</td><td>Ya tiene automatizaciones funcionando</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{closer("¿No sabe cuál elegir? Empiece con el diagnóstico gratuito.", "En 30 minutos le diremos qué opción le conviene, o si no necesita ninguna. Si la IA no es la solución a su problema, se lo diremos.")}
'''

# ================================================================= INDUSTRIAS
def fixes(rows):
    head = '<div class="fix fix--head" aria-hidden="true"><span>El problema</span><span>Cómo lo resolvemos</span><span>Funciona con</span></div>'
    body = "".join(
        f'<div class="fix" role="listitem"><p class="fix__problem">{p}</p><p class="fix__how">{h}</p><p class="fix__tools" data-label="Funciona con: ">{t}</p></div>'
        for p, h, t in rows)
    return f'<div class="fixes" role="list">{head}{body}</div>'

INDUSTRIES = f'''
<section class="page-hero aurora" aria-labelledby="in-title">
  <div class="wrap">
    <p class="label">Industrias · Problemas que resolvemos</p>
    <h1 id="in-title">Resolvemos los cuellos de botella que frenan su negocio.</h1>
    <p class="lead">Llamadas perdidas, seguimientos olvidados, papeleo fuera de horario, números que nunca ve. Esto es lo que resolvemos para restaurantes, empresas de servicios para el hogar y constructoras. Llámenos para una consulta gratuita y le diremos qué soluciones harán la mayor diferencia en su caso.</p>
    <nav class="jump" aria-label="Ir a una industria">
      <a href="#restaurants">{I["plate"]}Restaurantes</a><a href="#home-services">{I["thermo"]}HVAC y servicios para el hogar</a><a href="#construction">{I["hardhat"]}Construcción</a>
    </nav>
  </div>
</section>

<section class="section" style="padding-top:clamp(1.5rem,1rem + 2vw,2.5rem)">
  <div class="wrap">

    <div class="industry" id="restaurants">
      <div class="industry__head"><div class="stack"><p class="label">Restaurantes</p><h2>Más reservaciones, menos dolores de cabeza, mejores márgenes.</h2>
        <p class="lead">Para restaurantes, cafeterías, panaderías y servicios de banquetes. Las horas más ocupadas son cuando más se pierde, y ahí es exactamente donde funcionan estas soluciones.</p></div>
        <a class="btn btn--ghost" href="services.html#restaurants">Precios para restaurantes {A}</a></div>
      {fixes([
        ("Solicitudes de banquetes y eventos sin respuesta", "Cada llamada, formulario o mensaje de banquete recibe una respuesta inmediata que recopila fecha, número de invitados y presupuesto, y llega a su gerente como un resumen completo.", "Teléfono, sitio web, correo"),
        ("Reseñas sin contestar", "Respuestas redactadas con su voz para su aprobación. Los agradecimientos salen rápido; las quejas le llegan primero a usted.", "Google, Yelp"),
        ("Llamadas sin contestar en la hora de la cena", "El cliente recibe en segundos un mensaje amable con su enlace de reservaciones, su horario o una forma de dejar su solicitud.", "Su número de teléfono actual"),
        ("Horarios y menús que no coinciden en internet", "Actualice una vez; su sitio web y su perfil de Google cambian juntos, Yelp también, y una revisión semanal avisa si algo no coincide.", "Google, Yelp, su sitio web"),
        ("Mesas vacías por ausencias", "Mensajes de confirmación y recordatorio, y las cancelaciones se ofrecen automáticamente a su lista de espera.", "Sistema de reservaciones o formularios"),
        ("Empleados que faltan a última hora", "Los turnos disponibles se envían por texto al personal calificado; el primero que acepta lo cubre, con aprobación del gerente.", "7shifts, Homebase, lista de personal"),
        ("El costo de los alimentos sube sin que lo note", "Las facturas de proveedores se leen automáticamente, se marcan los aumentos de precio y recibe un reporte semanal de costo de alimentos.", "Facturas de Sysco, US Foods"),
        ("No sabe cómo le fue ayer", "Un mensaje cada mañana con ventas, porcentaje de mano de obra, cortesías, cancelaciones y lo más vendido.", "Toast, Square, Clover"),
        ("Los pagos de las apps de entrega no cuadran", "Los pagos se comparan con los pedidos y se marcan los reembolsos faltantes para que pueda reclamarlos.", "DoorDash, Uber Eats"),
        ("Clientes frecuentes que dejan de venir", "Mensajes de reconquista y de cumpleaños para clientes que aceptaron recibirlos.", "Datos de clientes de su punto de venta"),
      ])}
      <p class="caution">{I["info"]}<span>Las preguntas sobre alérgenos siempre las atiende su personal. Cualquier asistente que construyamos responde solo con su lista aprobada de alérgenos y le pide al cliente confirmar con su mesero.</span></p>
      {consult_cta("Administrar un restaurante ya es bastante trabajo. Déjenos quitarle parte de la carga.")}
    </div>

    <div class="industry" id="home-services">
      <div class="industry__head"><div class="stack"><p class="label">HVAC y servicios para el hogar</p><h2>Cierre más trabajos y dedique menos tiempo al papeleo.</h2>
        <p class="lead">Para empresas de aire acondicionado y calefacción, plomería, electricidad, techos y otros servicios a domicilio. La rapidez gana trabajos y el papeleo se come las ganancias.</p></div></div>
      {fixes([
        ("Solicitudes perdidas fuera de horario o durante un trabajo", "Cada llamada y formulario se registra, se clasifica y llega al teléfono de la persona indicada, y se escala hasta que alguien lo toma. Las llamadas por gas, humo o falta de calefacción van directo al técnico de guardia.", "Su teléfono, sitio web, Slack o texto"),
        ("Cotizaciones a las que nadie da seguimiento", "Las cotizaciones sin cerrar se siguen automáticamente a los 2, 5 y 10 días; las respuestas con interés van al vendedor.", "ServiceTitan, Housecall Pro, Jobber"),
        ("Contratos de mantenimiento que vencen", "Recordatorios de renovación y campañas de mantenimiento por temporada que agendan directo en su calendario.", "Lista de clientes, sistema de agenda"),
        ("Los técnicos odian el papeleo", "Una nota de voz de 30 segundos después de cada trabajo se convierte en un reporte limpio, un borrador de factura y un resumen para el cliente.", "App en el teléfono, software de trabajos"),
        ("Muy pocas reseñas en línea", "Una solicitud de reseña dos horas después de cada trabajo terminado; las respuestas de clientes molestos van al gerente en lugar de a Google.", "Google, software de trabajos"),
        ("Las mismas preguntas en cada visita", "Los técnicos consultan códigos de error y especificaciones en los manuales que usted cargue.", "Manuales de fabricantes"),
        ("No ve con claridad sus números", "Un reporte semanal de porcentaje de cierre, ticket promedio, visitas de garantía y desempeño de cada técnico.", "Su software de trabajos"),
      ])}
      {consult_cta("Sus técnicos deberían reparar equipos, no escribir notas. Hablemos.")}
    </div>

    <div class="industry" id="construction">
      <div class="industry__head"><div class="stack"><p class="label">Construcción</p><h2>Menos persecución, mejores registros, cobros más rápidos.</h2>
        <p class="lead">Para contratistas generales, remodeladores y subcontratistas especializados. La documentación y el seguimiento deciden si una obra deja ganancia.</p></div></div>
      {fixes([
        ("Las bitácoras diarias nunca se escriben", "Las fotos y notas de voz de la obra se convierten automáticamente en una bitácora diaria y un reporte semanal de avance.", "Teléfono, Google Drive, Buildertrend, Procore"),
        ("Órdenes de cambio que se pierden", "Las notas de campo se convierten en un borrador de orden de cambio enviado a firma electrónica el mismo día.", "Sus plantillas, firma electrónica"),
        ("Seguros de subcontratistas que vencen sin aviso", "Se vigila el certificado de seguro de cada subcontratista, con recordatorios antes del vencimiento y una alerta para retener pagos.", "Hoja de cálculo o correo"),
        ("Los clientes llaman a cada rato para saber cómo va", "Una actualización semanal redactada a partir de bitácoras y fotos, aprobada por usted antes de enviarla.", "Sus bitácoras diarias"),
        ("Invitaciones a licitar que se acumulan", "Cada invitación se resume con alcance, fecha límite y una lista para decidir si conviene participar.", "Correo"),
        ("Cobrar tarda demasiado", "Seguimiento programado de facturas vencidas, solicitudes de pago y renuncias de gravamen.", "QuickBooks"),
        ("Subcontratistas que llegan tarde o no llegan", "Mensajes de confirmación y recordatorio, y un aviso al gerente de proyecto cuando alguien va retrasado.", "Su programa de obra"),
      ])}
      {consult_cta("Dedique su tiempo a construir, no a perseguir papeles. Llámenos y le mostramos cómo.")}
    </div>
  </div>
</section>

{closer("Lo que sea que lo frene, resolvámoslo.", "Llámenos o reserve una consulta gratuita de 30 minutos. Cuéntenos en qué se le va la semana y le mostraremos qué resolver primero, cómo lo haríamos y cuánto vale. Si la IA no es la respuesta, también se lo diremos.")}
'''

# =============================================================== CASOS DE USO
def math_table(rows):
    body = "".join(
        f'<tr{" class=\"total\"" if i == len(rows) - 1 else ""}><td>{a}</td><td>{b}</td></tr>' for i, (a, b) in enumerate(rows))
    return f'<details class="math"><summary>Ver el cálculo y los supuestos</summary><div class="table-wrap"><table><tbody>{body}</tbody></table></div></details>'

USE_CASES = f'''
<section class="page-hero aurora" aria-labelledby="uc-title">
  <div class="wrap">
    <p class="label">Casos de uso</p>
    <h1 id="uc-title">Cómo se ve la IA dentro de un pequeño negocio</h1>
    <p class="lead">Un sistema que usamos todos los días y dos ejemplos desarrollados que muestran cómo funciona el mismo enfoque en un restaurante y en una empresa de servicios para el hogar. Cada uno presenta el reto, la solución y el resultado, con el cálculo a la vista para que lo cambie por sus propios números.</p>
    <div class="notice" role="note">{I["info"]}<p><b>Cómo leer estos casos.</b> El primero es nuestro propio sistema en funcionamiento. Los otros dos son ejemplos desarrollados con cifras típicas, no resultados de clientes. Publicaremos casos de clientes aquí cuando nos den permiso de compartirlos.</p></div>
  </div>
</section>

<section class="section" style="padding-top:clamp(1.5rem,1rem + 2vw,2.5rem)">
  <div class="wrap">

    <article class="case" aria-labelledby="c1">
      <div class="case__head">
        <div><p class="label">Sistema en funcionamiento · Servicios profesionales</p><h2 id="c1">Webcattus Labs: ninguna solicitud se queda esperando</h2>
          <p>Un estudio de una sola persona, donde el fundador suele estar en llamadas con clientes o lejos del escritorio cuando llegan nuevas solicitudes.</p></div>
        <span class="tag tag--live">Funcionando</span>
      </div>
      <div class="case__flow">
        <div class="case__col"><p class="label">Reto</p><ul>
          <li>Las solicitudes llegaban a una bandeja de entrada y esperaban hasta el siguiente descanso</li>
          <li>No había registro de qué tan rápido se respondía cada solicitud ni de su resultado</li>
          <li>Nadie más podía cubrir cuando el fundador estaba ocupado</li></ul></div>
        <div class="case__col"><p class="label">Solución con IA</p><ul>
          <li>Lead Router captura cada formulario del sitio y cada llamada perdida</li>
          <li>Reglas clasifican cada solicitud (urgente, cliente nuevo o existente) y envían una alerta al teléfono del fundador con un enlace para tomarla</li>
          <li>Las solicitudes sin atender se vuelven a avisar cada 30 minutos; un resumen llega a las 8 a. m.</li>
          <li>Se registra el resultado de cada una para los reportes</li></ul></div>
        <div class="case__col case__col--outcome"><p class="label">Resultado</p>
          <div class="metric"><b>Segundos</b><span>desde el envío del formulario hasta la alerta en el teléfono</span></div>
          <div class="metric"><b>0</b><span>solicitudes que puedan quedar sin ver: cada una se vuelve a avisar hasta que alguien la toma</span></div>
          <p class="small muted">Publicaremos los resultados de tiempo de respuesta y cierres después de 90 días de datos.</p></div>
      </div>
    </article>

    <article class="case" aria-labelledby="c2">
      <div class="case__head">
        <div><p class="label">Ejemplo desarrollado · Restaurante</p><h2 id="c2">Restaurante familiar: llamadas de banquetes perdidas en la hora de la cena</h2>
          <p>Un restaurante de 40 lugares con un negocio de banquetes en crecimiento. Las solicitudes de eventos llegan por teléfono, casi siempre entre las 5 y las 9 p. m., cuando nadie puede contestar.</p></div>
        <span class="tag">Ilustrativo</span>
      </div>
      <div class="case__flow">
        <div class="case__col"><p class="label">Reto</p><ul>
          <li>Unas 20 llamadas de banquetes y eventos al mes se van al buzón de voz</li>
          <li>Las llamadas se devuelven al día siguiente, cuando muchos clientes ya reservaron en otro lugar</li>
          <li>El personal pierde horas a la semana persiguiendo fecha, número de invitados y presupuesto</li></ul></div>
        <div class="case__col"><p class="label">Solución con IA</p><ul>
          <li>Mensaje de texto inmediato por cada llamada perdida</li>
          <li>Un asistente recopila por texto la fecha del evento, los invitados, el presupuesto y las restricciones alimentarias</li>
          <li>El gerente recibe un resumen completo con un enlace para tomarlo; se escala si nadie responde en 15 minutos</li>
          <li>Se generan borradores de cotización con el menú de banquetes para que el gerente los apruebe</li></ul></div>
        <div class="case__col case__col--outcome"><p class="label">Resultado estimado</p>
          <div class="metric"><b>≈$2,600</b><span>en ventas de banquetes recuperadas al mes</span></div>
          <div class="metric"><b>≈4 h</b><span>menos de llamadas de ida y vuelta por semana</span></div>
          <div class="metric"><b>≈2.5 meses</b><span>para recuperar la implementación (con base en ventas)</span></div></div>
      </div>
      {math_table([
        ("Llamadas de banquetes o eventos perdidas al mes", "20"),
        ("Contactadas con el mensaje inmediato (60%)", "12"),
        ("Reservadas, una de cada tres contactadas", "4"),
        ("Pedido promedio de banquete", "$650"),
        ("Implementación: agente enfocado / mensual: plan Esencial", "$4,500 / $750"),
        ("Ventas recuperadas al mes (4 × $650)", "$2,600"),
      ])}
    </article>

    <article class="case" aria-labelledby="c3">
      <div class="case__head">
        <div><p class="label">Ejemplo desarrollado · Servicios para el hogar</p><h2 id="c3">Empresa de HVAC: solicitudes fuera de horario y papeleo de oficina</h2>
          <p>Una empresa de calefacción y aire acondicionado con seis técnicos. Las solicitudes de noche y de fin de semana se acumulan, y la gerente de oficina pasa las mañanas convirtiendo mensajes de voz en órdenes de trabajo.</p></div>
        <span class="tag">Ilustrativo</span>
      </div>
      <div class="case__flow">
        <div class="case__col"><p class="label">Reto</p><ul>
          <li>Unas 40 solicitudes al mes llegan fuera de horario; solo la mitad recibe respuesta el mismo día</li>
          <li>Los trabajos urgentes, como "no tengo calefacción", quedan en el mismo buzón que las preguntas de rutina</li>
          <li>Seis horas a la semana copiando datos entre el buzón de voz, el correo y el sistema de agenda</li></ul></div>
        <div class="case__col"><p class="label">Solución con IA</p><ul>
          <li>Reglas detectan palabras de urgencia y seguridad, y avisan de inmediato al técnico de guardia</li>
          <li>Las solicitudes de rutina se guardan y se asignan a las 8 a. m., con un respaldo y luego el dueño si nadie las toma</li>
          <li>La IA convierte cada llamada y formulario en un resumen claro dentro del sistema de agenda</li>
          <li>Gas, humo o chispas siempre van a una persona con la indicación "llamar ya"</li></ul></div>
        <div class="case__col case__col--outcome"><p class="label">Resultado estimado</p>
          <div class="metric"><b>≈5</b><span>trabajos más reservados al mes</span></div>
          <div class="metric"><b>≈$2,250</b><span>en ingresos adicionales al mes</span></div>
          <div class="metric"><b>≈6 h</b><span>menos de papeleo de oficina por semana</span></div></div>
      </div>
      {math_table([
        ("Solicitudes fuera de horario al mes", "40"),
        ("Contactadas el mismo día hoy (50%)", "20"),
        ("Contactadas el mismo día con distribución y escalamiento (90%)", "36"),
        ("Clientes adicionales contactados", "16"),
        ("Porcentaje de cierre de solicitudes contactadas", "30%"),
        ("Ticket promedio", "$450"),
        ("Ingresos adicionales al mes (≈5 trabajos × $450)", "$2,250"),
      ])}
    </article>
  </div>
</section>

{closer("¿Quiere ver cómo se vería con sus números?", "Traiga al diagnóstico gratuito un conteo aproximado de sus llamadas, solicitudes y horas de papeleo. Haremos el mismo tipo de estimación para su negocio, y le diremos con claridad si los números no dan.")}
'''

# ==================================================================== NOSOTROS
ABOUT = f'''
<section class="page-hero aurora" aria-labelledby="ab-title">
  <div class="wrap">
    <p class="label">Acerca de Webcattus Labs</p>
    <h1 id="ab-title">Experiencia de gran empresa en IA, a la medida del negocio local.</h1>
    <p class="lead">Webcattus Labs es una consultora de IA con sede en Dallas para pequeños negocios. Aplicamos los métodos que usan las grandes empresas para automatizar el trabajo y hacerlo confiable, con un alcance y un precio pensados para equipos de 2 a 50 personas.</p>
  </div>
</section>

<section class="section" aria-labelledby="founder-title">
  <div class="wrap founder">
    <figure class="portrait" style="margin:0" aria-label="Espacio para la foto del fundador">J<figcaption>Fundador</figcaption></figure>
    <div class="prose">
      <p class="label">Fundador</p>
      <h2 id="founder-title">Hola, soy Jay.</h2>
      <p>Soy ingeniero de datos. Durante casi cuatro años construí y automaticé sistemas de datos en producción para una empresa de salud del Fortune 10, incluidos los procesos detrás de los modelos de suscripción de beneficios farmacéuticos, con PySpark, Databricks y Google Cloud. Ese trabajo me enseñó qué hace confiable a una automatización: reglas claras, pruebas cuidadosas y una persona a cargo de todo lo importante.</p>
      <p>La mayoría de los pequeños negocios nunca tiene acceso a ese nivel de ingeniería. Reciben un montón de aplicaciones que no se conectan entre sí o una presentación de ventas llena de tecnicismos. Webcattus Labs existe para cerrar esa brecha. Cada sistema se configura bien, se explica en palabras sencillas y se mide contra un número que a usted le importa.</p>
      <p>Cuando trabaja con Webcattus Labs, trabaja directamente conmigo: la persona que define su proyecto es la misma que lo construye y la que contesta el teléfono después.</p>
      <div class="facts">
        <div class="fact"><b>Certificado en Google Cloud</b><span>Professional Data Engineer y Professional Cloud Architect</span></div>
        <div class="fact"><b>Certificado en Databricks</b><span>Data Engineer Professional</span></div>
        <div class="fact"><b>Certificación PMP®</b><span>Proyectos bien definidos, programados y entregados a tiempo</span></div>
        <div class="fact"><b>Investigador publicado</b><span>12 artículos arbitrados, Premio Springer al Mejor Artículo (ICSSCC 2026), revisor activo</span></div>
        <div class="fact"><b>Maestría en Gestión de TI</b><span>The University of Texas at Dallas</span></div>
        <div class="fact"><b>Ingeniería Mecánica (B.Tech)</b><span>SRM, con colaboración en investigación en IIT Madras</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint" aria-labelledby="phil-title">
  <div class="wrap">
    <div class="section-head">
      <p class="label">Nuestra filosofía de IA</p>
      <h2 id="phil-title">Lo útil vale más que lo impresionante.</h2>
      <p class="lead">La IA es una herramienta, no una estrategia. Estas convicciones guían lo que recomendamos y aquello de lo que convencemos a nuestros clientes de no hacer.</p>
    </div>
    <div class="grid-2">
      <div class="card"><h3>Empezar por el problema, no por la tecnología</h3><p>Comenzamos por entender en qué se le va la semana y dónde se le escapan los clientes. A veces la respuesta es IA. A veces es un mejor formulario o una regla sencilla, y se lo diremos.</p></div>
      <div class="card"><h3>Medirlo todo</h3><p>Cada proyecto tiene una meta acordada antes de empezar: horas ahorradas, tiempo de respuesta o ingresos recuperados. Si no se puede medir, no lo vendemos.</p></div>
      <div class="card"><h3>Las personas siguen al mando</h3><p>La IA redacta, clasifica y recuerda. Las personas aprueban precios, atienden quejas y toman las decisiones. Todo lo relacionado con seguridad va directo a una persona.</p></div>
      <div class="card"><h3>Sin ataduras</h3><p>Todo queda en cuentas a su nombre y con documentación. Debería seguir trabajando con nosotros porque le conviene, no porque no tenga otra opción.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="who-title">
  <div class="wrap proof">
    <div class="stack">
      <p class="label">Con quién trabajamos</p>
      <h2 id="who-title">Negocios dirigidos por sus dueños, de 2 a 50 personas</h2>
      <p class="lead">Sobre todo restaurantes, empresas de servicios para el hogar y despachos profesionales en Dallas–Fort Worth. Trabajamos a distancia en todo Estados Unidos.</p>
    </div>
    <div class="stack">
      <h3>Buena opción si</h3>
      {check_list(["Pierde clientes u horas en trabajo repetitivo", "Quiere resultados medibles, no un experimento", "Puede dedicarnos una hora a la semana durante la implementación"])}
      <h3 style="margin-top:.6rem">Probablemente no sea para usted si</h3>
      {check_list(["Quiere que la IA tome decisiones sin revisión humana", "Necesita una gran plataforma interna", "Busca el chatbot más barato posible"], "checks checks--x")}
    </div>
  </div>
</section>

{closer("Hablemos de su negocio, no de IA.", "Cuéntenos en qué se le va la semana. Le diremos con honestidad qué vale la pena automatizar y qué no.")}
'''

# ==================================================================== PREGUNTAS
def qa(q, a):
    return f'<details class="qa"><summary><span>{q}</span><span class="pm" aria-hidden="true">+</span></summary><div class="answer">{a}</div></details>'

FAQ = f'''
<section class="page-hero aurora" aria-labelledby="faq-title">
  <div class="wrap">
    <p class="label">Preguntas frecuentes</p>
    <h1 id="faq-title">Respuestas directas sobre la IA en su negocio</h1>
    <p class="lead">Las preguntas que más nos hacen los dueños: sobre datos, precisión, costo y tiempos. Si la suya no está aquí, hágala en la llamada de diagnóstico gratuito.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(1.5rem,1rem + 2vw,2.5rem)">
  <div class="wrap faq-layout">
    <nav class="faq-nav" aria-label="Temas">
      <a href="#privacy">Datos y privacidad</a><a href="#accuracy">Precisión y control</a><a href="#timeline">Tiempos y costos</a><a href="#working">Cómo trabajamos</a>
    </nav>
    <div>
      <div class="faq-group"><h2 id="privacy">Datos y privacidad</h2>
        {qa("¿Qué pasa con los datos de mi negocio y de mis clientes?", "<p>Se quedan en sus cuentas. Solo conectamos los sistemas que el proyecto necesita, y solo los campos necesarios. Los datos de sus clientes no se copian a hojas de cálculo ni a instrucciones de IA a menos que la tarea lo requiera.</p><p>Antes del lanzamiento recibe un mapa de datos de una página que muestra qué se conecta, a dónde van los datos y quién puede verlos.</p>")}
        {qa("¿Usarán mis datos para entrenar modelos de IA?", "<p>Usamos planes empresariales y de API de proveedores de IA reconocidos cuyos términos establecen que su información no se usa para entrenar sus modelos. Le mostramos esos términos antes de que apruebe el proyecto.</p>")}
        {qa("¿Quién tiene acceso a mis sistemas?", "<ul><li>Las cuentas se crean a su nombre, no al nuestro.</li><li>Usamos el acceso mínimo que cada tarea necesita, y usted puede retirarlo cuando quiera.</li><li>Nunca le pediremos contraseñas por correo. El acceso se comparte con su administrador de contraseñas o con el sistema de invitaciones de cada herramienta.</li><li>Cuando termina un proyecto, nuestro acceso termina también, salvo que tenga un plan de asesoría.</li></ul>")}
        {qa("¿Pueden trabajar con información médica, legal o financiera?", "<p>A veces, con cuidado. Si un proceso involucra información regulada, como expedientes médicos protegidos por HIPAA, solo avanzamos cuando están en su lugar las herramientas y los acuerdos que exige. Se lo señalaremos en el diagnóstico, y preferimos rechazar un proyecto antes que tomar atajos.</p>")}
      </div>

      <div class="faq-group"><h2 id="accuracy">Precisión y control</h2>
        {qa("¿Qué pasa si la IA inventa algo?", "<p>Es un riesgo real, por eso lo prevenimos desde el diseño:</p><ul><li><b>Respuestas fundamentadas:</b> los asistentes responden solo con la información que usted aprobó, como su menú, su lista de precios y sus políticas.</li><li><b>Alcance limitado:</b> cada agente hace bien una sola tarea en lugar de intentar responderlo todo.</li><li><b>Pasa a una persona si tiene dudas:</b> si una pregunta está fuera de lo que sabe, lo dice y la pasa a su equipo.</li><li><b>Probado antes del lanzamiento:</b> con al menos 50 ejemplos reales de su negocio, incluidos los difíciles.</li><li><b>Revisado después:</b> las conversaciones se registran y se revisan cada mes.</li></ul>")}
        {qa("¿Podría decirle algo vergonzoso a un cliente?", "<p>Todo lo que se envía en su nombre usa textos que usted aprobó o pasa primero por una persona. Las quejas, los reembolsos, los precios y los temas de seguridad siempre se envían a su equipo.</p>")}
        {qa("¿Pueden actualizar Yelp y publicar respuestas a reseñas automáticamente?", "<p>En parte. El perfil de empresa de Google permite que herramientas aprobadas actualicen horarios y publiquen respuestas a reseñas, así que eso se hace con un toque. Yelp limita lo que pueden cambiar las herramientas externas, así que para Yelp le preparamos la actualización o la respuesta exacta y usted la publica desde su cuenta de Yelp en unos segundos. Una revisión semanal avisa si algún perfil deja de coincidir.</p>")}
        {qa("¿En qué no es buena la IA?", "<p>En decisiones de criterio, conversaciones delicadas, tareas donde un error sale caro y procesos cuyas reglas cambian cada semana. Le diremos cuándo una tarea le corresponde a una persona, o a una regla sencilla en lugar de IA.</p>")}
      </div>

      <div class="faq-group"><h2 id="timeline">Tiempos y costos</h2>
        {qa("¿Cuánto tarda en estar funcionando?", "<ul><li><b>Diagnóstico de IA:</b> 30 minutos, normalmente dentro de la semana en que reserva.</li><li><b>Taller de descubrimiento:</b> un día, con su reporte tres días hábiles después.</li><li><b>Agente enfocado:</b> listo en 2 a 3 semanas. <b>Agente conectado:</b> de 3 a 5 semanas.</li><li><b>Paquete para restaurantes:</b> de 1 a 3 semanas.</li></ul>")}
        {qa("¿Cuánto cuesta mantenerlo funcionando?", "<p>La mayoría de los proyectos cuesta unas decenas de dólares al mes en tarifas de herramientas y uso, que paga directamente a los proveedores a su nombre. Verá una estimación antes de aprobar cualquier cosa. El soporte continuo es opcional y comienza en $750 al mes.</p>")}
        {qa("¿Cómo sabré si está funcionando?", "<p>Antes de empezar acordamos una meta, como tiempo de respuesta, horas ahorradas o trabajos reservados. Recibe un reporte mensual breve frente a esa meta, generado con los registros del propio sistema.</p>")}
        {qa("¿Qué pasa si no se alcanza la meta?", "<p>Averiguamos por qué y lo corregimos. Si aun así no vale la pena mantenerlo, le recomendaremos apagarlo. Los planes de asesoría son mes a mes, así que nunca paga por algo que no le da resultados.</p>")}
      </div>

      <div class="faq-group"><h2 id="working">Cómo trabajamos</h2>
        {qa("¿Necesito personal técnico?", "<p>No. Nosotros nos encargamos de la configuración y la parte técnica. Necesitamos a alguien que conozca el proceso durante una hora a la semana mientras construimos, y una breve capacitación antes del lanzamiento.</p>")}
        {qa("¿La IA va a reemplazar a mis empleados?", "<p>No es así como lo diseñamos. La meta es quitarles las partes repetitivas de su trabajo, como las llamadas de ida y vuelta, copiar datos entre aplicaciones o contestar la misma pregunta por décima vez, para que dediquen más tiempo a los clientes y al trabajo que solo ellos pueden hacer.</p>")}
        {qa("¿Solo trabajan en Dallas–Fort Worth?", "<p>Estamos en Dallas y con gusto vamos en persona a cualquier punto de DFW. Todo lo demás funciona a distancia, en cualquier lugar de Estados Unidos.</p>")}
        {qa("¿Qué herramientas de IA usan?", "<p>Las que mejor se adapten al trabajo y a las herramientas por las que ya paga. No somos revendedores ni cobramos comisiones de software, así que nuestras recomendaciones no dependen de ningún proveedor.</p>")}
      </div>
    </div>
  </div>
</section>

{closer("¿Le queda alguna pregunta?", "Tráigala al diagnóstico gratuito de 30 minutos. Recibirá una respuesta directa y una idea clara de dónde la IA podría ayudar a su negocio.")}
'''

# ==================================================================== CONTACTO
def opts(pairs):
    # value (English, for the Slack alert) → visible Spanish label
    return "".join(f'<option value="{_html.escape(v)}">{l}</option>' for v, l in pairs)

def chips(name, pairs):
    return '<div class="chips">' + "".join(
        f'<label class="chip"><input type="checkbox" name="{name}" value="{_html.escape(v)}"><span>{l}</span></label>' for v, l in pairs) + "</div>"

CONTACT_PAGE = f'''
<section class="page-hero aurora" aria-labelledby="ct-title">
  <div class="wrap">
    <p class="label">Diagnóstico de IA</p>
    <h1 id="ct-title">Reserve su diagnóstico de IA gratuito</h1>
    <p class="lead">Cuéntenos un poco sobre su negocio y elija un horario. En 30 minutos sabrá qué tareas vale la pena automatizar, cuánto vale aproximadamente cada una y qué se necesita.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(1rem,.5rem + 1.5vw,2rem)">
  <div class="wrap contact-layout">
    <div class="form-card">
      <div class="progress" aria-label="Progreso de la reservación">
        <span class="pill is-current">1 · Sobre su negocio</span><span aria-hidden="true">→</span><span class="pill">2 · Elija un horario</span>
      </div>

      <form id="booking-form" method="POST"
            action="https://lead-router.webcattus.workers.dev/form/webcattus?redirect=https%3A%2F%2Fwebcattuslabs.com%2Fes%2Fcontact.html">
        <fieldset class="fieldset">
          <legend>Sobre usted</legend>
          <div class="fields">
            <div class="field"><label for="f-name">Nombre completo</label><input id="f-name" name="name" type="text" autocomplete="name" required maxlength="120"></div>
            <div class="field"><label for="f-email">Correo electrónico</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="160"></div>
            <div class="field"><label for="f-company">Nombre del negocio</label><input id="f-company" name="company" type="text" autocomplete="organization" required maxlength="120"></div>
            <div class="field"><label for="f-phone">Teléfono <span class="opt">(opcional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="30"></div>
            <div class="field field--full"><label for="f-site">Sitio web <span class="opt">(opcional)</span></label><input id="f-site" name="site_url" type="url" inputmode="url" placeholder="https://" maxlength="200"></div>
          </div>
        </fieldset>

        <fieldset class="fieldset">
          <legend>Sobre su negocio</legend>
          <div class="fields">
            <div class="field"><label for="f-industry">Industria</label>
              <select id="f-industry" name="industry" required><option value="">Elija una</option>{opts([
                ("Restaurant or food & beverage", "Restaurante o alimentos y bebidas"), ("Home services", "Servicios para el hogar"),
                ("Construction", "Construcción"), ("Professional services", "Servicios profesionales"),
                ("Health & wellness", "Salud y bienestar"), ("Retail or e-commerce", "Comercio o tienda en línea"),
                ("Real estate", "Bienes raíces"), ("Other", "Otra")])}</select></div>
            <div class="field"><label for="f-size">Tamaño del equipo</label>
              <select id="f-size" name="team_size" required><option value="">Elija una opción</option>{opts([
                ("Just me", "Solo yo"), ("2–10 people", "2 a 10 personas"), ("11–50 people", "11 a 50 personas"), ("51–200 people", "51 a 200 personas")])}</select></div>
            <div class="field field--full"><span class="field__label" id="drains-label">¿En qué se le va el tiempo? <span class="opt">Elija todas las que apliquen</span></span>
              <div role="group" aria-labelledby="drains-label">{chips("drains", [
                ("Missed calls & slow replies", "Llamadas perdidas y respuestas lentas"), ("Catering & private events", "Banquetes y eventos privados"),
                ("Online reviews", "Reseñas en línea"), ("Hours & menu listings", "Horarios y menú en internet"),
                ("Scheduling & booking", "Agenda y reservaciones"), ("Quotes & proposals", "Cotizaciones y propuestas"),
                ("Data entry & admin", "Captura de datos y papeleo"), ("Customer questions", "Preguntas de clientes"),
                ("Marketing & content", "Marketing y contenido"), ("Not sure yet", "Todavía no estoy seguro")])}</div></div>
            <div class="field"><label for="f-budget">Presupuesto para un primer proyecto</label>
              <select id="f-budget" name="budget"><option value="">Prefiero no decirlo</option>{opts([
                ("Under $2,500", "Menos de $2,500"), ("$2,500–$7,500", "$2,500 a $7,500"), ("$7,500–$15,000", "$7,500 a $15,000"),
                ("$15,000+", "Más de $15,000"), ("Not sure yet", "Todavía no lo sé")])}</select>
              <span class="hint">Nos ayuda a sugerirle el mejor punto de partida.</span></div>
            <div class="field"><label for="f-timeline">¿Cuándo quiere empezar?</label>
              <select id="f-timeline" name="timeline"><option value="">Elija una opción</option>{opts([
                ("As soon as possible", "Lo antes posible"), ("Within 1–3 months", "En 1 a 3 meses"), ("In 3–6 months", "En 3 a 6 meses"), ("Just exploring", "Solo estoy explorando")])}</select></div>
            <div class="field field--full"><label for="f-message">¿Qué le gustaría resolver primero? <span class="opt">(opcional)</span></label>
              <textarea id="f-message" name="message" maxlength="2000" placeholder="Por ejemplo: perdemos llamadas de banquetes durante la cena y yo paso los domingos en la noche haciendo facturas."></textarea></div>
          </div>
        </fieldset>

        <div class="hp" aria-hidden="true"><label for="f-hp">Deje este campo vacío</label><input id="f-hp" name="website_hp" type="text" tabindex="-1" autocomplete="off"></div>
        <input type="hidden" name="_elapsed" value="">

        <div class="form-foot">
          <button class="btn btn--primary" type="submit">Enviar y elegir horario {A}</button>
          <p class="small muted">Solo usaremos estos datos para preparar su llamada. Sin boletines.</p>
        </div>
        <p class="form-status" role="alert" hidden></p>
      </form>

      <div class="booked" hidden tabindex="-1" role="status" aria-live="polite">
        <span class="mark">{I["check"]}</span>
        <h2 data-hello>Gracias. Recibimos sus datos.</h2>
        <p>Último paso: elija un horario de 30 minutos que le convenga. Recibirá una invitación de calendario con el enlace de video.</p>
        <a class="btn btn--primary" data-calendar hidden href="#" target="_blank" rel="noopener">Elegir horario {A}</a>
        <p data-no-calendar>Le enviaremos dos o tres opciones de horario por correo en un día hábil. ¿Prefiere hablar antes? Escríbanos a <b>{EMAIL}</b>.</p>
        <p class="small muted" data-preview hidden>Modo de vista previa: no se envió nada. En webcattuslabs.com este formulario llega directo a Lead Router.</p>
      </div>
    </div>

    <aside class="side" aria-label="Qué esperar">
      <div class="card">
        <h3>Qué pasa en la llamada</h3>
        <ol>
          <li>Nos cuenta cómo es una semana normal: en qué se va el tiempo y dónde se escapan los clientes.</li>
          <li>Le señalamos las dos o tres tareas que más vale la pena automatizar.</li>
          <li>Recibe una estimación aproximada de horas o ingresos para cada una, y qué se necesita.</li>
        </ol>
      </div>
      <div class="card">
        <h3>Se lleva</h3>
        {check_list(["Un resumen por escrito en un día hábil", "Consejos honestos, incluso cuando la IA no es la respuesta", "Sin compromiso y sin campañas de ventas"])}
      </div>
      <div class="card">
        <h3>¿Prefiere hablar ahora?</h3>
        <p>Llame o envíe un mensaje de texto al <a href="tel:{PHONE_E164}"><b>{PHONE_DISPLAY}</b></a>, de lunes a viernes, de 9 a. m. a 6 p. m., hora del centro. Si no alcanzamos a contestar, le devolvemos la llamada el mismo día.</p>
        <div class="copyline"><code>{PHONE_DISPLAY}</code><button class="copy-btn" type="button" data-copy="{PHONE_DISPLAY}">Copiar</button></div>
      </div>
      <div class="card">
        <h3>¿Prefiere escribirnos?</h3>
        <div class="copyline"><code>{EMAIL}</code><button class="copy-btn" type="button" data-copy="{EMAIL}">Copiar</button></div>
        <p class="small muted">Respuesta en un día hábil, de la persona que haría el trabajo.</p>
      </div>
    </aside>
  </div>
</section>
'''

PAGES = [
  {"path": "index.html", "title": "Webcattus Labs · IA para pequeños negocios", "body": HOME,
   "desc": "Consultoría de IA para pequeños negocios en Dallas–Fort Worth. Automatizamos el seguimiento, el papeleo y las preguntas de clientes, con una meta medible en horas ahorradas o ingresos recuperados."},
  {"path": "services.html", "title": "Servicios y precios · Webcattus Labs", "body": SERVICES,
   "desc": "Taller de descubrimiento de IA, agentes de IA a la medida, paquete para restaurantes y asesoría mensual para pequeños negocios. Entregables claros y precios fijos."},
  {"path": "industries.html", "title": "Industrias · Webcattus Labs", "body": INDUSTRIES,
   "desc": "Los cuellos de botella que resolvemos para restaurantes, empresas de HVAC y servicios para el hogar, y constructoras. Llame para una consulta gratuita."},
  {"path": "use-cases.html", "title": "Casos de uso · Webcattus Labs", "body": USE_CASES,
   "desc": "Cómo funcionan el seguimiento y la automatización con IA dentro de un pequeño negocio: reto, solución y resultado, con el cálculo a la vista."},
  {"path": "about.html", "title": "Nosotros · Webcattus Labs", "body": ABOUT,
   "desc": "Webcattus Labs lleva la experiencia en ingeniería de datos de las grandes empresas a los pequeños negocios. Conozca al fundador y nuestro enfoque de IA práctica y responsable."},
  {"path": "faq.html", "title": "Preguntas frecuentes · Webcattus Labs", "body": FAQ,
   "desc": "Respuestas sobre IA para pequeños negocios: privacidad de datos, seguridad, precisión, tiempos y costos."},
  {"path": "contact.html", "title": "Reserve su diagnóstico de IA · Webcattus Labs", "body": CONTACT_PAGE,
   "desc": "Reserve un diagnóstico de IA gratuito de 30 minutos con Webcattus Labs."},
]
