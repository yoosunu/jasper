import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getMessaging, getToken } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging.js";
import { onMessage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging.js";

// importScripts("https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging.js");
// importScripts("https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging.js");

const firebaseConfig = {
    apiKey: "AIzaSyAMXUlfzQUNzIKHFHDQdT8VLyJoIBfyZBI",
    authDomain: "pusher-d134f.firebaseapp.com",
    projectId: "pusher-d134f",
    storageBucket: "pusher-d134f.appspot.com",
    messagingSenderId: "708144789790",
    appId: "1:708144789790:web:66afc5997333cc7dd5310f",
    measurementId: "G-5TL2LN3GNZ",
    databaseURL: "https://pusher-d134f-default-rtdb.firebaseio.com/"
  }; 

  // Initialize Firebase
const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);
// const database = getDatabase(app); 

// cloud tokening
        // Add the public key generated from the console here.
        getToken(messaging, 
            {vapidKey: "BAJV03StYOSJ3em2Kue33M_hve7X2aVvyzcxLFT7ff1JgMsuPBR-9S8rRVp0wrmdMkEoqWTnFN0JH2I2XA1rKJ0"});

          function requestPermission() {
            console.log('Requesting permission...');
            Notification.requestPermission().then((permission) => {
              if (permission === 'granted') {
                console.log('Notification permission granted.')}})};
    
            // Get registration token. Initially this makes a network call, once retrieved
            // subsequent calls to getToken will return from cache.
            getToken(messaging, { vapidKey: 'BAJV03StYOSJ3em2Kue33M_hve7X2aVvyzcxLFT7ff1JgMsuPBR-9S8rRVp0wrmdMkEoqWTnFN0JH2I2XA1rKJ0' }).then((currentToken) => {
              if (currentToken) {
                // Send the token to your server and update the UI if necessary
                localStorage.setItem('my token', currentToken)
                // ...
              } else {
                // Show permission request UI
                console.log('No registration token available. Request permission to generate one.');
                // ...
              }
            }).catch((err) => {
              console.log('An error occurred while retrieving token. ', err);
              // ...
            });
        requestPermission()

// cloud messaging when forground
// const messaging = getMessaging();
        document.getElementById('codemax').addEventListener('click', (event) => {
        event.preventDefault()
        onMessage(messaging, (payload) => {
            console.log('Message received. ', payload);
            // ...
        });
        });
 