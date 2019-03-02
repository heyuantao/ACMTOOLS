import React from "react";
import Login from "./Login"

class LoginPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
        }
    }
    componentDidMount() {
    }
    render() {
        return (
            <div style={{ padding: 24, background: "#fff"}}>
                <Login></Login>
            </div>
        )
    }
}

export default LoginPage