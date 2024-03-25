import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
        // console.log(e.target.value);
    };
    const handleSubmit = () => {
        axios
            .post('http://localhost:8000/submit-code/', { code: inputValue })
            .then((response) => {
                console.log(response.data);
            })
            .catch((error) => {
                console.error('There was an error!', error);
            });
    };

    return (
        <div className="App">
            <div className="header">
                <h1>FunctionNameGenerator</h1>
            </div>
            <div className="wrapper">
                <textarea
                    type="text"
                    placeholder="your code"
                    className="input-box"
                    value={inputValue}
                    onChange={handleInputChange}
                />
                <button className="submit-btn" onClick={handleSubmit}>
                    submit your code
                </button>
            </div>
            <div className="bottom"></div>
        </div>
    );
}

export default App;
