import logo from './logo.svg';
import './App.css';
import {useEffect,useState} from 'react'

function App() {

  const [data, setData] = useState('Initializing...')

  useEffect(() => {
    
    const sse = new EventSource('/stream')

    function handleStream(e){
      console.log(e)
      setData(e.data)
    }

    sse.onmessage = e =>{handleStream(e)}

    sse.onerror = e => {
      //GOTCHA - can close stream and 'stall'
      sse.close()
    }

    return () => {
      sse.close()
      
    }
  }, )  

  return (
    <div className="App">
     The last streamed item was: {data}
    </div>
  );
}

export default App;
