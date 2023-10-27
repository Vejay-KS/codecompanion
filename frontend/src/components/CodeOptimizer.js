import React, { useState } from 'react';
import axios from 'axios';
import { API_URL } from '../constants';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "xcsrftoken";

const CodeOptimizerFormUI = () => {
  const [inputCode, setInputCode] = useState('');
  const [codeCompletion, setCodeCompletion] = useState('');

  const handleSubmit = async (e) => {
    console.log("check");
    e.preventDefault();

    try {
      const response = await axios.post(API_URL, {
        input_code: inputCode,
      });
      const { code_completion } = response.data;
      setCodeCompletion(code_completion);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <input type="text" value={inputCode} onChange={(e) => setInputCode(e.target.value)} />
      <button onClick={handleSubmit}>Generate Code Completion</button>
      <div>{codeCompletion}</div>
    </div>
  );
};

export default CodeOptimizerFormUI;