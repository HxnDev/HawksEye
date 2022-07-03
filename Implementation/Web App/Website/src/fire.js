import firebase from 'firebase';

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyDihLI0AWX1mgkkhuS-iqX2uO5_CwH_YvI",
  authDomain: "hospitalaid-f6855.firebaseapp.com",
  projectId: "hospitalaid-f6855",
  storageBucket: "hospitalaid-f6855.appspot.com",
  messagingSenderId: "700688388064",
  appId: "1:700688388064:web:a58ffe819a4794e7dee585"
};

  // Initialize Firebase
  const fire = firebase.initializeApp(firebaseConfig);

  export default fire;