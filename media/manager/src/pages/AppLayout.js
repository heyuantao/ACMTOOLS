import React from "react";
import {Router,Route,hashHistory,IndexRedirect} from "react-router";
import App from "./App";
import AntiCheatingPage from "./AntiCheatingPage";
import AntiCheatingAnalyzeResultPage from "./AntiCheatingAnalyzeResultPage";
import CodeExportPage from "./CodeExportPage";
import PersonalPage from "./PersonalPage";


export default class AppLayout extends React.Component{
    handleOnEnter(){
    }
    render(){
        return(
            <Router history={hashHistory} >
                <Route path="/" component={App}>
                    <IndexRedirect to="/anticheating/contestsubmit" ></IndexRedirect>
                    <Route path="/anticheating/contestsubmit/:contest_id/analyze" component={AntiCheatingAnalyzeResultPage} onEnter={this.handleOnEnter}></Route>
                    <Route path="/anticheating/contestsubmit" component={AntiCheatingPage} onEnter={this.handleOnEnter}></Route>
                    <Route path="/codeexport" component={CodeExportPage} onEnter={this.handleOnEnter}></Route>
                    <Route path="/personal" component={PersonalPage} onEnter={this.handleOnEnter}></Route>
                </Route>
            </Router>
        );
    }
}