import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import LIForm from './Insecure.jsx' 
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <LIForm />
  </StrictMode>,
)
