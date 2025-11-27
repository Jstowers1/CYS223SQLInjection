import React, {useState} from 'react';


export default function LIFormSec(){
  const [formData, setFormData] = useState({name: '', email: '', password: ''})
  const [message, setMessage]   = useState('');

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
      const response = await fetch('http://localhost:5000/submitSec', {
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
      <h4>A form NOT vulnerable to SQL Injection</h4>
      <form onSubmit={handleSubmit}>
        <div>
          <label for = "name">NAME</label> <br />
          <input type="text" name="name" value={formData.name} onChange={handleChange}/>
          <p> Wow... since I'm a secure form it doesn't matter what kind of weird data gets put into me!</p>
        </div>
        <div>
          <label for = "email">EMAIL</label> <br />
          <input type="text" name="email" value={formData.email} onChange={handleChange}/>
        </div>
        <div>
          <label for = "password">PASSWORD</label> <br />
          <input type="text" name="password" value={formData.password} onChange={handleChange}/>
        </div>
        <button type="submit">SUBMIT</button> <br />
      </form>
      {message && <p> Server Response: **{message}**</p>}
    </div>
  )
}
