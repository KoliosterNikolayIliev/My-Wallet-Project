import React from "react";
import unsupportedImg from "../../images/its-so-small-i-cant-see-it.jpg";


const UnsupportedResolution = () => {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      flexDirection: 'column',
      width:'80%'
    }}>
      <h2 style={{color: '#9031db',textAlign:'center'}}>Unsupported resolution !!!</h2>
      <div style={{width:'100%'}}>
        <img style={{
          objectFit: 'cover',
          width: '100%',
          height: 'auto'
        }} src={unsupportedImg} alt="Unsupported!"/>
      </div>
      <h2 style={{color: '#9031db',textAlign:'center'}}>We're sure you have a bigger screen !!! &#128513;</h2>
    </div>
  );
};

export default UnsupportedResolution;
