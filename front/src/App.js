import React, { useState } from 'react';
import './App.css';

function App() {
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
        console.log(e.target.value);
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
                <button className="submit-btn">submit your code</button>
            </div>
            <div className="bottom"></div>
        </div>
    );
}

export default App;
