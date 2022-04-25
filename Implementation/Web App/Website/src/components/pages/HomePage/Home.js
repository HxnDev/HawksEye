import React, {useEffect} from 'react';
import axios from 'axios';
import HeroSection from './HeroSection';

function Home() {

    // this runs when react page loads
    useEffect( () => {
        axios.get('http://localhost:5000/init').then(response => {
            console.log("SUCCESS", response)
        }).catch(error => {
            console.log(error)
        })

    }, [])

  return (
    <>
      <HeroSection />
    </>
  );
}

export default Home;