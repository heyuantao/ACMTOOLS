import React from "react";
import {Router,Route,hashHistory,IndexRedirect} from "react-router";
import App from "./App";
import LoginPage from "./LoginPage";


export default class AppLayout extends React.Component{
    handleOnEnter(){
    }
    render(){
        return(
            <Router history={hashHistory} >
                <Route path="/" component={App}>
                    <IndexRedirect to="/login" ></IndexRedirect>
                    <Route path="/login" component={LoginPage} onEnter={this.handleOnEnter}></Route>
                </Route>
            </Router>
        );
    }
}