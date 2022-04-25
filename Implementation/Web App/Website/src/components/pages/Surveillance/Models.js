import React, { useEffect, useState } from 'react'
import './Models.css';
import axios from 'axios';
import { IconContext } from 'react-icons/lib';

function Models() {

  const [selectedModel, setSelectedModel] = useState('');

  // this is dependent on selectedModel var updating
  useEffect(() => {
    console.log(selectedModel, ' selected');

    if (selectedModel.length > 0) {
      sendModelToFlask().then(r => {
        console.log('Sent model to flask');
      });
    }
  }, [selectedModel]);

  // send selected model data to flask server
  async function sendModelToFlask() {
    const formData = new FormData();
    // you can append your own stuff here if you want to
    formData.append('type', selectedModel);

    // so now I send formData (which has the stuff I want to send to flask)
    await axios.post('http://localhost:5000/selectModel', formData).then(response => {
      console.log("response reply: ", response);
      console.log(selectedModel, "model selected in flask");
    }).catch(error => {
      console.error(error.response.data);
    })
  }

  // update the selection
  function selectModel(event, model) {
    event.preventDefault();
    setSelectedModel(model);
  }

  return (
    
    <IconContext.Provider value={{ color: '#fff', size: 64 }}>
      <div className='models__section'>
        <div className='models__wrapper'>
          <div className='models__container'>
            
            <button onClick={(event) => selectModel(event, 'face-mask')} className='models__container-card' >
              <div className='models__container-cardInfo'>
                <h4>Face Mask</h4>
              </div>
            </button>
            
            <button onClick={(event) => selectModel(event, 'yolo-social-dist')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Social Distancing Monitoring</h4>
              </div>
            </button>
            
            <button onClick={(event) => selectModel(event, 'yolo-empty')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Empty Counter</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'car-parking')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Empty Parking</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'activity-faint')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Fainting</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'activity-choke')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Choking</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'activity-drowsy')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Drowsiness</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'activity-aggressive')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Aggressive Behaviour</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'face-attendance')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Facial Attendance</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'activity-smoking')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Smoking</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'yolo-weapon')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Weapon</h4>
              </div>
            </button>

            <button onClick={(event) => selectModel(event, 'yolo-person')} className='models__container-card'>
              <div className='models__container-cardInfo'>
                <h4>Isolation Ward</h4>
              </div>
            </button>

          </div>
        </div>
      </div>
    </IconContext.Provider>
  );
}

export default Models