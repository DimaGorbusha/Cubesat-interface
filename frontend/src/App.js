import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { SignUp } from './Pages/SignUp';
import { ListTests } from './Pages/ListTests';
import { TestDetail } from './Pages/TestDetail';
import { CreateTest } from './Pages/CreateTest';

function App() {
  return (
    <div className="App">
      <Router>
            <Routes>
                <Route path='/' element={<SignUp />} />
                <Route path='/list-tests' element={<ListTests />} />
                <Route path='/test-detail' element={<TestDetail />} />
                <Route path='/create-test' element={<CreateTest />} />
            </Routes>
        </Router>
    </div>
  );
}

export default App;
