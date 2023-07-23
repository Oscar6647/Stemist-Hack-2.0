const CLIENT_ID = '25078404912-0f27h541nemdtvbvkn8csuqnsbku1b5a.apps.googleusercontent.com'; 
const API_KEY = 'AIzaSyAvK-_venbKyg1hMvY8myxfM-KDhlBstzo'; 
const DISCOVERY_DOC = 'https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest';
const SCOPES = 'https://www.googleapis.com/auth/calendar.events';

let tokenClient;
let gapiInited = false;
let gisInited = false;

document.getElementById('eventForm').style.display = 'none';

function gapiLoaded() {
  gapi.load('client', initializeGapiClient);
}

async function initializeGapiClient() {
  await gapi.client.init({
    apiKey: API_KEY,
    discoveryDocs: [DISCOVERY_DOC],
  });
  gapiInited = true;
  maybeEnableButtons();
}

function gisLoaded() {
  tokenClient = google.accounts.oauth2.initTokenClient({
    client_id: CLIENT_ID,
    scope: SCOPES,
    callback: '', 
  });
  gisInited = true;
  maybeEnableButtons();
}

function maybeEnableButtons() {
  if (gapiInited && gisInited) {
    document.getElementById('authorize_button').style.visibility = 'visible';
  }
}

function handleAuthClick() {
  tokenClient.callback = async (resp) => {
    if (resp.error !== undefined) {
      throw (resp);
    }
    document.getElementById('signout_button').style.visibility = 'visible';
    document.getElementById('authorize_button').innerText = 'Refrescar';
    document.getElementById('eventForm').style.display = 'block';
    await listUpcomingEvents();
  };

  if (gapi.client.getToken() === null) {
    tokenClient.requestAccessToken({ prompt: 'consent' });
  } else {
    tokenClient.requestAccessToken({ prompt: '' });
  }
}

function handleSignoutClick() {
  const token = gapi.client.getToken();
  if (token !== null) {
    google.accounts.oauth2.revoke(token.access_token);
    gapi.client.setToken('');
    document.getElementById('content').innerText = '';
    document.getElementById('eventForm').style.display = 'none';
    document.getElementById('authorize_button').innerText = 'Autorizar';
    document.getElementById('signout_button').style.visibility = 'hidden';
  }
}

async function listUpcomingEvents() {
  let response;
  try {
    const request = {
      'calendarId': 'primary',
      'timeMin': (new Date()).toISOString(),
      'showDeleted': false,
      'singleEvents': true,
      'maxResults': 10,
      'orderBy': 'startTime',
    };
    response = await gapi.client.calendar.events.list(request);
  } catch (err) {
    document.getElementById('content').innerText = err.message;
    return;
  }

  const events = response.result.items;
  if (!events || events.length == 0) {
    document.getElementById('content').innerText = 'No Events Found';
    return;
  }
  // Mostrar eventos en la página
  let output = 'Next Events:\n';
  events.forEach((event) => {
    const startTime = event.start.dateTime || event.start.date;
    output += `${event.summary} (${startTime})\n`;
  });
  document.getElementById('content').innerText = output;
}

function createEvent() {
    const eventTitle = document.getElementById('eventTitle').value;
    const eventDate = document.getElementById('eventDate').value;
    const eventStartTime = document.getElementById('eventStartTime').value;
    const eventEndTime = document.getElementById('eventEndTime').value;
    const eventLocation = document.getElementById('eventLocation').value;
  
    const event = {
      summary: eventTitle,
      start: {
        dateTime: `${eventDate}T${eventStartTime}:00`,
        timeZone: 'UTC', 
      },
      end: {
        dateTime: `${eventDate}T${eventEndTime}:00`,
        timeZone: 'UTC', 
      },
      location: eventLocation,
    };
  
    gapi.client.calendar.events.insert({
      calendarId: 'primary',
      resource: event,
    }).then((response) => {
      console.log('Evento creado:', response);
      alert('El evento se ha creado exitosamente en Google Calendar.');
    }).catch((error) => {
      console.error('Error al crear el evento:', error);
      alert('Error al crear el evento en Google Calendar.');
    });
  }
