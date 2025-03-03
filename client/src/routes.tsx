import { RouteObject } from "react-router-dom";
import Welcome from "./Welcome";
import Login from "./login";
import Signup from "./Signup";

const routes: RouteObject[] = [
  { path: "/", element: <Welcome /> },
  { path: "/login", element: <Login />},
  { path: "/signup", element: <Signup />}
];

export default routes;
