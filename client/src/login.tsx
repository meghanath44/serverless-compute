import { useState } from "react";
import { useNavigate } from "react-router-dom";

interface loginRes{
    isSuccess : boolean
}

function Login(){

    let navigate = useNavigate();
    let [username, setUsername] = useState('');
    let [password, setPassword] = useState('');
    let [loginDetails, setLoginDetails] = useState('');
    const PATH = "http://localhost:4000";

    let onClickLogin =function(event: React.FormEvent<HTMLFormElement>){
        event.preventDefault();
        fetch(`${PATH}/login`,{
            method : 'POST',
            mode : 'cors',
            body : JSON.stringify({
                username : username,
                password : password
            })
        }).then(data => data.json()).then(data => validateAndLogin(data));
    }

    let validateAndLogin = (data: loginRes) => {
        if(data.isSuccess){
            navigate('../home');
        }
        else{
            setPassword('');
            setLoginDetails('Invalid Credentials');
        }
    }

    return(
        <div className="login">
            <header className="header">
                <div></div>
                <div></div>
                <div>
                    <button onClick={() => navigate('../')}>Home</button>
                </div>
            </header>
            <div className="login-container">
                <div className="login-box">
                    <form onSubmit={(event)=>onClickLogin(event)}>
                        <div className="input-group">
                            <label htmlFor="username">Username</label>
                            <input type="text" id="username" placeholder="Enter username" onChange={(event)=>setUsername(event.currentTarget.value)} value={username}></input>
                        </div>
                        <div className="input-group">
                            <label htmlFor="password">Password</label>
                            <input type="password" id="password" placeholder="Enter password" onChange={(event)=>setPassword(event.currentTarget.value)} value={password}></input>
                        </div>
                        <br></br>
                        <div className="loginDetails">{loginDetails}</div>
                        <button type="submit" className="login-btn">Login</button>
                        <br></br>
                        <br></br>
                        <div>If you don't have an account! <a href="./Signup">Signup</a></div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Login;