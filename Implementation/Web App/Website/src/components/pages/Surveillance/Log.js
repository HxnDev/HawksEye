import React, { useState, useEffect, } from 'react';
import './Log.css';
import fire from '../../../fire';

function Log() {

    const db = fire.firestore();

    const [detectionList, setDetectionList] = useState([]);

    useEffect(() => {
        const unsubscribe = fire
            .firestore().collection('detections')
            .orderBy('time')
            .onSnapshot(snapshot => {
                if (snapshot.size) {
                    let arr = [];
                    snapshot.docs.map((doc) =>
                        arr.push(doc.data())
                    );

                    setDetectionList(arr)
                    console.log(detectionList);
                } else {
                    console.log('no data in firebase');
                }
            })
        return () => {
            unsubscribe()
        }
    }, [fire])

    return (
      <>
          <div className='log-container'>
              <div className='text'>
                  {detectionList.map((detection) => (
                      <h1 className='heading-text' key={detection['id']}>
                          <span>{detection['time'].toDate().toLocaleDateString('en-GB')} {detection['time'].toDate().toLocaleTimeString()}</span> {detection['type']}
                      </h1>
                  ))}
              </div>
          </div>
      </>
    );
  }

  export default Log;
