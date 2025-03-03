import { useNavigate } from "react-router-dom";

function welcome(){

    const navigate = useNavigate();

    return (
        <div>
            <header className="header">
                <div></div>
                <div></div>
                <div>
                    <button onClick={() => navigate('./login')}>Login</button>
                    <button onClick={() => navigate('./signup')}>Signup</button>
                </div>
            </header>
            <div className="welcome">
                <h2>Serverless Cloud Computing Project</h2>
            </div>
        </div>
    );
} 

export default welcome; 