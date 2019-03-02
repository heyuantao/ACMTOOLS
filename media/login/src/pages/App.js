import React from "react";
import { Layout, Row } from "antd";

const { Content} = Layout;

export default class App extends React.Component{
    render(){
        return(
            <div >
                <Row type="flex" justify="center" align="middle" style={{marginTop:"250px"}}></Row>
                {this.props.children}
            </div>
        );
    }
}