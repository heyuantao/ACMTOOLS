import React from "react";
import {connect} from "react-redux";
import {fromJS} from "immutable";
import {hashHistory} from "react-router";
import * as LocationActionCreator from "../Common/store/LocationIndicatorActionCreator";
import {Button, Col, Row, Tabs} from "antd";
import OneAccountWithMultiIP from "./OneAccountWithMultiIP";
import OneIPWithMultiAccount from "./OneIPWithMultiAccount";

const TabPane = Tabs.TabPane;

class AntiCheatingAnalyzeResultPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            contest_id:this.props.params.contest_id,
        }
    }
    componentDidMount() {
        this.props.showLocation()
    }
    handleBack(){
        hashHistory.push("/anticheating/contestsubmit");
    }
    handleTabSelected(key) {
        console.log(key);
    }
    render() {
        return (
            <div style={{ padding: 24, background: "#fff"}}>
                <Row type="flex" justify="space-between" align="middle" >
                    <Col>
                        <h2>查看分析结果(考试编号为：{this.state.contest_id})</h2>
                    </Col>
                    <Col>
                        <Button onClick={()=>{this.handleBack()}} type="primary">返回</Button>
                    </Col>
                </Row>
                <Row type="flex" justify="space-between" align="middle">
                    <Col span={24}>
                        <div style={{ marginBottom: "15px" }}></div>
                        <Tabs defaultActiveKey="1"  type="card"
                              onChange={(key)=>{this.handleTabSelected(key)}}>
                            <TabPane tab="单账号多IP" key="1">
                                <OneAccountWithMultiIP contest_id={this.props.params.contest_id}></OneAccountWithMultiIP>
                            </TabPane>
                            <TabPane tab="单IP多账号" key="2">
                                <OneIPWithMultiAccount contest_id={this.props.params.contest_id}></OneIPWithMultiAccount>
                            </TabPane>
                        </Tabs>
                    </Col>
                </Row>
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        showLocation(locationList){
            dispatch(LocationActionCreator.changeLocation(fromJS(["作弊分析","替考分析","分析结果"])))
        }
    }
}

export default connect(null,mapDispatchToProps)(AntiCheatingAnalyzeResultPage)