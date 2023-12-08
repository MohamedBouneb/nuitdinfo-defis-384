import React from 'react';
import '../components/Solution.css'
import { useState , useEffect } from 'react';
export const Solution = () => {

    const [message, setMessage] = useState('');

  useEffect(() => {
    fetch("http://localhost:5000/weather") 
      .then(response => response.json())
      .then(data =>{
        setMessage(data)
        console.log(data); 
      } )
      .catch(error => console.error('Error:', error))
  }, [])

  return (
    <div className="content">
      <div className="txt"><p>Ce modèle anticipe également les conditions climatiques requises pour cultiver le 
        fruit optimal dans ce contexte climatique {message} </p></div>



    
    </div>
  );
};