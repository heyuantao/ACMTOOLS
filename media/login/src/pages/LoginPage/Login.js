import React from "react";
import {hashHistory, Link} from "react-router";
import { Row, Col, Form, Button, Table, Icon} from 'antd';
import { fromJS } from "immutable";
import Settings from "../../Settings";

const FormItem = Form.Item;
const req = Settings.request;
const table_data_api_url = Settings.anti_cheating_contest_api_url;

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }
    componentWillReceiveProps(props) {
        //this.fetchTableListData()
    }
    render() {
        return (
            <div>
                <Row type="flex" justify="space-between" align="middle" >
                    <Col>
                        <h2>考试提交数据分析</h2>
                    </Col>
                    <Col>
                        <Button onClick={() => { this.handleFetchTableData() }} type="primary" >刷新</Button>
                    </Col>
                </Row>
                <Row type="flex" justify="space-between" align="middle">
                    <Col span={24}>
                        <div style={{ marginBottom: "15px" }}></div>
                    </Col>
                </Row>
            </div>
        )
    }
}

export default Login