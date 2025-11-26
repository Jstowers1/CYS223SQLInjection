import React, {useState} from 'react';


export default function LIForm(){
  const [formData, setFormData] = useState({name: '', email: ''})
  const [message, setMessage]   = useState('');

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
      const response = await fetch('http://localhost:5000/submitInsec', {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error('Error submitting form. ', error);
      setMessage('Failed to connect to server');
    }
  };
/*
  const sayHello = async () => {
    try{
      event.preventDefault();
      const res = await fetch("http://localhost:5000/hello");
      const data = await res.json();
      console.log(data.message);
    } catch (err) {
      console.log(err);
    }
  }
*/
  return(
    <div>
      <p>Maybe this time it'll work...?</p>
      <form onSubmit={handleSubmit}>
        <div>
          <label for = "name">Enter username here pls :3</label> <br />
          <input type="text" name="name" value={formData.name} onChange={handleChange}/>
        </div>
        <div>
          <label for = "email">Enter the email here x3</label> <br />
          <input type="text" name="email" value={formData.email} onChange={handleChange}/>
        </div>
        <button type="submit">Submit here brochado</button> <br />
      </form>
      {message && <p> Server Response: **{message}**</p>}
    </div>
  )
}
