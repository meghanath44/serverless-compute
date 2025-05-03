import { useLocation, useNavigate } from "react-router-dom";
import React, {useState, useEffect, useRef} from "react";

function Home(){
    const navigate = useNavigate();
    const [open, setOpen] = useState(false);
    const [create, setCreate] = useState(false);
    const [view, setView] = useState(false);
    const dropdownRef = useRef<HTMLDivElement>(null);
    const location = useLocation();
    const [selectedItem, setSelectedItem] = useState("Machine configuration");

    const toggleDropdown = () => setOpen(!open);

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if(dropdownRef.current && !dropdownRef.current.contains(event.target as Node)){
                setOpen(false);
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const menuItems = [
        "Machine configuration",
        "OS and storage",
        "Data protection",
        "Networking",
        "Observability",
        "Security",
        "Advanced",
    ];

    useEffect(() => {
        setOpen(false);
    }, [location]);

    const handleCreate = () => {
        setOpen(false);
        setView(false);
        setCreate(true);
    };

    const handleView = () => {
        setOpen(false);
        setCreate(false);
        setView(true);
    };

    const setMainContent = () => {

    }

    return (
        <div>
            <header className="header">
                <div className="header-left" ref={dropdownRef}>
                    <button onClick={toggleDropdown} className="dropdown-toggle">☰ Instances</button>
                    {open && (
                        <div className="dropdown-menu">
                            <div onClick={handleCreate}>Create</div>
                            <div onClick={handleView}>View</div>
                        </div>
                    )}
                </div>
                <div className="header-center"></div>
                <div className="header-right">
                    <button onClick={() => navigate('../')}>Logout</button>
                </div>
            </header>
            <div>
                {create && (
                    <div className="container">
                        <div className="sidebar">
                            <ul>
                                {menuItems.map((item) => (
                                    <li key={item} onClick={() => setSelectedItem(item)}>
                                        {item}
                                    </li>
                                ))}
                            </ul>
                        </div>
                        <div className="main-content">
                            <h2>{selectedItem}</h2>
                        </div>
                        <div className="side-info">
                            <h3>Monthly estimate</h3>
                            <p></p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Home;