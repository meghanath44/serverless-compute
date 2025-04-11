import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Signup(){

    let onClickSignUp = function(event: React.FormEvent<HTMLFormElement>){
        event.preventDefault();
    }
    let navigate = useNavigate();
    let [userName, setUserName] = useState('');
    let [password, setPassword] = useState('');
    let [rePassword, setRePassword] = useState('');
    let [signUpDetails, setSignUpDetails] = useState('');

    return(
        <div className="signUp">
            <header className="header">
                <div></div>
                <div></div>
                <div>
                    <button onClick={() => navigate('../')}>Home</button>
                </div>
            </header>
            <div className="login-container">
                <div className="login-box">
                    <form onSubmit={(event)=>onClickSignUp(event)}>
                        <div className="input-group">
                            <label htmlFor="username">Email Address</label>
                            <input type="text" id="username" placeholder="Enter username" onChange={(event)=>setUserName(event.currentTarget.value)} value={userName}></input>
                        </div>
                        <div className="input-group">
                            <label htmlFor="password">Password</label>
                            <input type="password" id="password" placeholder="Enter password" onChange={(event)=>setPassword(event.currentTarget.value)} value={password}></input>
                        </div>
                        <div className="input-group">
                            <label htmlFor="re-password">Confirm Password</label>
                            <input type="password" id="re-password" placeholder="Re-enter password" onChange={(event)=>setRePassword(event.currentTarget.value)} value={rePassword}></input>
                        </div>
                        <br></br>
                        <div className="SignUpDetails">{signUpDetails}</div>
                        <button type="submit" className="signup-btn">SignUp</button>
                        <br></br>
                        <br></br>
                        <div>If you already have an account! <a href="./Login">Login</a></div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Signup;