import React from "react";
import { Layout } from "antd";
import SideBar from "./Common/SideBar";
import PageHeader from "./Common/PageHeader";
import PageFooter from "./Common/PageFooter"
import LocationIndicator from "./Common/LocationIndicator";

const { Content} = Layout;

export default class App extends React.Component{
    render(){
        return(
             <Layout style={{ minHeight: "100vh" }}>
                    <SideBar></SideBar>
                    <Layout>
                        <PageHeader></PageHeader>
                        <LocationIndicator></LocationIndicator>
                        <Content style={{ margin: "0 10px" }}>
                            {this.props.children}
                        </Content>
                        <PageFooter></PageFooter>
                    </Layout>
                </Layout>
        );
    }
}