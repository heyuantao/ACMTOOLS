import React from "react";
import {hashHistory, Link} from "react-router";
import { Row, Col, Form, Button, Table, Icon, Input, Alert} from 'antd';
import { fromJS } from "immutable";
import Utils from "../Common/Utils";
import Settings from "../../Settings";

const FormItem = Form.Item;
const req = Settings.request;
const table_data_api_url = Settings.anti_cheating_contest_api_url;

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            formData:fromJS({}),

        }
    }
    handleLoginSubmit() {
        if (this.validateFormField() < 0) {
            return
        }
        req.post(Settings.loginAPIURL, this.state.formData.toJS()).then(function (response) {
            if (response.data.dashboardurl != undefined) {
                window.location.href = response.data.dashboardurl;
            }
        }.bind(this)).catch(function (error) {
        }.bind(this))

    }

    validateFormField() {
        let formData = this.state.formData;
        this.setState({ formFieldValidateInfo: "" })

        if (!formData.get("email")) {
            this.setState({ formFieldValidateInfo: "用户名不能为空！" })
            return -1
        }
        if (!Utils.isEmailValid(formData.get("email"))) {
            this.setState({ formFieldValidateInfo: "用户名格式不正确 ！" })
            return -1
        }
        if (!formData.get("password")) {
            this.setState({ formFieldValidateInfo: "请输入密码 ！" })
            return -1
        }
        if ( formData.get("email").length> 20) {
            this.setState({ formFieldValidateInfo: "用户名非法 ！" })
            return -1
        }
        const formFieldMaxLength = fromJS({"email":25,"password":30,"captcha":10})
        let result = Utils.formFieldLengthCheck(this.state.formData,formFieldMaxLength)
        if(result!==""){
            this.setState({ formFieldValidateInfo: result })
            return -1
        }
        return 1
    }
    handleFieldChange(value, field) {
        let dict = {}; dict[field] = value;
        let change = fromJS(dict);
        this.setState({ formData: this.state.formData.merge(change) }, () => { this.validateFormField() })
    }

    render() {
        const formData = this.state.formData;
        return (
            <div>
                <Row type="flex" justify="center" align="middle" >
                    <Col md={{ span: 8 }}>
                        <h1 style={{ height: "60px", lineHeight: "60px", color: "black", textAlign: "center" }}>ACM数据分析</h1>
                    </Col>
                </Row>
                <Row type="flex" justify="center" align="middle" >
                    <Col md={{ span: 6 }}>
                        <Form className="login-form">
                            <FormItem>
                                <Input  onBlur={(e) => { this.handleFieldChange(e.target.value, "email") }}
                                    prefix={<Icon type="user" style={{ fontSize: 13 }} />} placeholder="请输入用户名" size="large" />
                            </FormItem>
                            <FormItem>
                                <Input onBlur={(e) => { this.handleFieldChange(e.target.value, "password") }}
                                    prefix={<Icon type="lock" style={{ fontSize: 13 }} />} type="password" placeholder="请输入密码" size="large" />
                            </FormItem>
                            <FormItem hasFeedback >
                                {(this.state.formFieldValidateInfo != "") &&
                                    <Alert message={this.state.formFieldValidateInfo} type="error" />
                                }
                            </FormItem>
                            <FormItem>
                                <Row type="flex" justify="end" align="middle">
                                    <Button type={this.state.formFieldValidateInfo === "" ? "primary" : "disabled"}
                                        onClick={() => { this.handleLoginSubmit() }} className="login-form-button">
                                        登录系统
                                    </Button>
                                </Row>
                            </FormItem>
                        </Form>
                    </Col>
                </Row>
            </div>

        )
    }
}

export default Login