import { useLocation, useNavigate } from "react-router-dom";
import React, {useState} from "react";
import Modal from "./Modal";

interface ServiceConfig{
    userName : string,
    serviceName : string,
    imageUrl : string,
    region : string,
    port : number,
    hashValue : string
}

function generateRandomHash(length: number): string {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        result += characters.charAt(randomIndex);
    }
    
    return result;
}


function Home(){
    const navigate = useNavigate();

    const location = useLocation();
    const { username } = location.state as {username : string};
    const [selectedItem, setSelectedItem] = useState("Create");
    const [serviceName, setServiceName] = useState<string>("");
    const [imageUrl, setImageUrl] = useState<string>("");
    const [region, setRegion] = useState<string>("Indiana");
    const [port, setPort] = useState<number>(80);
    const [listOfServices, setlistOfServices] = useState<ServiceConfig[]>([]);
    const [showModal, setShowModal] = useState(false);
    const PATH = "http://localhost:4000";

    const menuItems = [
        "Create",
        "View"
    ];

    const ImageUrls = [
        "custom-nginx:latest",
        "httpd:latest",
        "apache-ubuntu:latest",
        "hello-node:latest",
        "react-test:latest",
        "my-react-app:latest"
    ];

    const Regions = [
        "Indiana",
        "Iowa",
        "California"
    ];

    const setValuesToDefault = () => {
        setServiceName("");
        setImageUrl("");
        setRegion("Indiana");
        setPort(80);
    }

    const handleSubmit = (e : React.FormEvent) => {
        e.preventDefault();
        let newService : ServiceConfig  = {
            userName : username,
            serviceName : serviceName,
            imageUrl : imageUrl,
            region : region,
            port : port,
            hashValue : generateRandomHash(8)
        }
        setlistOfServices(prev => [...prev , newService]);
        setShowModal(true);
        fetch(`${PATH}/createService`,{
            method : 'POST',
            mode : 'cors',
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify({
                userName : username,
                serviceName : serviceName,
                imageUrl : imageUrl,
                region : region,
                port : port,
                hashValue : newService.hashValue
            })
        }).then(data => data.json());
        setValuesToDefault();
        console.log({ username, serviceName, imageUrl, region, port });
    }

    return (
        <div>
            <header className="header">
                <div className="header-left"><b>Hi {username}!</b></div>
                <div className="header-center"></div>
                <div className="header-right">
                    <button onClick={() => navigate('../')}>Logout</button>
                </div>
            </header>
            <div>
                <div className="container">
                    <div className="sidebar">
                        <h3>Services</h3>
                        <ul>
                            {menuItems.map((item) => (
                                <div>
                                <hr></hr>
                                <li key={item} onClick={() => setSelectedItem(item)}>
                                    {item}
                                </li>
                                </div>
                            ))}
                            <hr></hr>
                        </ul>
                    </div>
                    <div className="main-content">
                        {(selectedItem == "Create"?
                            (
                                <div>
                                    <h2>Create Service</h2>
                                    <form className="form-container" onSubmit={handleSubmit}>
                                        <label>
                                            Service name * :
                                            <input type="text" value={serviceName} onChange={
                                                (e) => setServiceName(e.currentTarget.value)
                                            } required></input>
                                        </label>
                                        <label>
                                            Container Image URL * :
                                            <select value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} required>
                                                <option value="">Select</option>
                                                {ImageUrls.map((item) => (
                                                    <option value={item}>{item}</option>
                                                ))}
                                            </select>
                                        </label>
                                        <label>
                                            Region * :
                                            <select value={region} onChange={(e) => setRegion(e.target.value)}>
                                                {Regions.map((item) =>( 
                                                    <option value={item}>{item}</option>
                                                ))}
                                            </select>
                                        </label>
                                        <label>
                                            Port * :
                                            <input type="number" value={port} onChange={(e) => setPort(parseInt(e.target.value))} required/>
                                        </label>
                                        <div className="form-actions">
                                            <button type="submit" className="create-button">Create</button>
                                            <button type="button" className="cancel-button">Cancel</button>
                                        </div>
                                    </form>
                                    {showModal && (<Modal message="Service created successfully!" onClose={()=> setShowModal(false)}></Modal>)}
                                </div>
                            ):(
                                <div>
                                    <table className="service-table">
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th>Name</th>
                                                <th>Region</th>
                                                <th>Image URL</th>
                                                <th>Last Deployed</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {listOfServices.map( (service,index) => (
                                                <tr key={index}>
                                                     <td>{index+1}</td>
                                                     <td><a href={"https://"+service.serviceName+"-"+service.hashValue+".csci-b516.me"} target="_blank">{service.serviceName}</a></td>
                                                     <td>{service.region}</td>
                                                     <td>{service.imageUrl}</td>
                                                     <td>05-05-2025</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            )
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Home;