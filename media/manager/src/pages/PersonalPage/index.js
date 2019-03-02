import React from "react";
import {Link} from "react-router";
import { Row, Col, Icon, Form, Input, Button, Alert, message, Spin} from 'antd';
import { fromJS } from "immutable";
import Settings from "../../Settings";

const FormItem = Form.Item;
const req = Settings.request

class PersonalPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fetching: false,
            formData: fromJS({}),
            formFieldValidateInfo: "",
        }
    }
    componentDidMount(){
        this.fetchData()
    }
    fetchData(){
        let url = Settings.user_api_url;
        this.setState({fetching:true});
        req.get(url,{}).then((response)=>{
            const data = fromJS(response.data);
            this.setState({formData:data});
            this.setState({fetching:false});
        }).catch((error)=>{
            this.setState({fetching:false});
        })
    }
    validateForm() {
        let formData = this.state.formData;
        this.setState({ formFieldValidateInfo: "" })
        if ((formData.get("password") === undefined) || (formData.get("password") === "")) {
            this.setState({ formFieldValidateInfo: "密码不能为空 ！" });
            return -1;
        }
        if ((formData.get("repeat_password") === undefined) || (formData.get("repeat_password") === "")) {
            this.setState({ formFieldValidateInfo: "密码不能为空 ！" });
            return -1;
        }
        if (formData.get("repeat_password") != formData.get("password")) {
            this.setState({ formFieldValidateInfo: "密码不相同 ！" });
            return -1;
        }
        if (formData.get("password").length < 6) {
            this.setState({ formFieldValidateInfo: "密码小于六位 ！" });
            return -1;
        }
        return 1
    }
    handleFieldChange(value, field) {
        let dict = {}; dict[field] = value;
        let change = fromJS(dict);
        this.setState({ formData: this.state.formData.merge(change) }, () => { this.validateForm() })
    }
    handlePasswordChangeSubmit() {
        const formData = this.state.formData;
        if(this.validateForm()<0){
            return;
        }
        const url = Settings.user_api_url;
        req.put(url,this.state.formData.toJS()).then((response)=>{
            let data = fromJS(response.data);
            message.success('密码修改成功');
            this.fetchData();
        })
    }
    render() {
        let formData = this.state.formData;
        const formItemLayout = { labelCol: { xs: { span: 24 }, sm: { span: 8 }, }, wrapperCol: { xs: { span: 24 }, sm: { span: 16 }, }, };
        const tailFormItemLayout = { wrapperCol: { xs: { span: 24, offset: 0, }, sm: { span: 16, offset: 8, }, }, };
        const fetching = this.state.fetching;
        return (
            <div style={{ padding: 24, background: '#fff' }}>
                <Row type="flex" justify="space-between" align="middle" >
                    <Col>
                        <h2>密码修改</h2>
                    </Col>
                    <Col>
                        {(fetching)&&<Spin></Spin>}
                    </Col>
                </Row>
                <Row>
                    <div style={{ marginTop: "30px" }}></div>
                </Row>
                <Row type="flex" justify="space-around" align="middle" >
                    <Col span={8}>
                        <Form className="login-form">
                            <FormItem {...formItemLayout} label="用户名" >
                                <Input value={formData.get("username")} disabled={true}
                                    prefix={<Icon type="user" style={{ fontSize: 13 }} />}  placeholder="请输入密码" />
                            </FormItem>
                            <FormItem {...formItemLayout} label="请输入密码" required={true}>
                                <Input value={formData.get("password")} onChange={(e) => { this.handleFieldChange(e.target.value, "password") }}
                                    prefix={<Icon type="eye-invisible" style={{ fontSize: 13 }} />} type="password" placeholder="请输入密码" />
                            </FormItem>
                            <FormItem {...formItemLayout} label="再次输入密码" required={true}>
                                <Input value={formData.get("repeat_password")} onChange={(e) => { this.handleFieldChange(e.target.value, "repeat_password") }}
                                    prefix={<Icon type="eye-invisible" style={{ fontSize: 13 }} />} type="password" placeholder="请输再次输入密码" />
                            </FormItem >
                            <FormItem hasFeedback {...tailFormItemLayout} >
                                {(this.state.formFieldValidateInfo !== "") &&
                                    <Alert message={this.state.formFieldValidateInfo} type="error" />
                                }
                            </FormItem>
                            <FormItem {...tailFormItemLayout}>
                                <Row type="flex" justify="end" align="middle">
                                    <Link to="/examination" style={{marginRight:"10px"}}>
                                        <Button>取消</Button>
                                    </Link>
                                    <Button onClick={() => { this.handlePasswordChangeSubmit() }} className="login-form-button"
                                        type={this.state.formFieldValidateInfo === "" ? 'primary' : 'disabled'}>
                                        确定
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

export default PersonalPage