import { RouteObject } from "react-router-dom";
import Welcome from "./welcome";
import Login from "./Login";
import Signup from "./Signup";
import Home from "./home";

const routes: RouteObject[] = [
  { path: "/", element: <Welcome /> },
  { path: "/login", element: <Login />},
  { path: "/signup", element: <Signup />},
  { path: "/home", element: <Home />}
];

export default routes;
