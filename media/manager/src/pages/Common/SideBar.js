import React from "react";
import { hashHistory,Link } from "react-router";
import { Icon, Layout, Menu } from "antd";
import {connect} from "react-redux";
import {fromJS} from "immutable";
import * as LocationActionCreator from "./store/LocationIndicatorActionCreator";
const { Header, Content, Footer, Sider } = Layout;
const SubMenu = Menu.SubMenu;

class SideBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedKeys:["11"],
        }
    }
    componentDidMount(){
        let that = this;
        hashHistory.listen( (location) =>  {
            if(location.action==="PUSH"){
                if(location.pathname.includes("/anticheating/contestsubmit")){
                    that.setState({selectedKeys:["11"]});
                    this.props.changeLocation(fromJS(["作弊分析","替考分析"]));
                    return;
                }
                if(location.pathname.includes("/codeexport")){
                    that.setState({selectedKeys:['21']});
                    this.props.changeLocation(fromJS(["试卷管理","代码导出"]));
                    return;
                }
                if(location.pathname.includes("/personal")){
                    that.setState({selectedKeys:['91']});
                    this.props.changeLocation(fromJS(["个人管理","密码修改"]));
                    return;
                }
            }
        });
    }
    render() {
        return (
            <Sider width="230">
                <div className="logo" style={{textAlign:"center"}} >
                    <h1 style={{color:"white"}}>数据分析</h1>
                </div>
                <Menu theme="dark" defaultSelectedKeys={["1"]} defaultOpenKeys={["sub1"]}
                      selectedKeys={this.state.selectedKeys} mode="inline">
                    <SubMenu key="sub1" title={<span><Icon type="pie-chart" /><span>作弊分析</span></span>}>
                        <Menu.Item key="11">
                            <Link to="/anticheating/contestsubmit">
                                <Icon type="schedule" /><span>替考分析</span>
                            </Link>
                        </Menu.Item>
                    </SubMenu>
                    <SubMenu key="sub2" title={<span><Icon type="contacts" /><span>试卷管理</span></span>}>
                        <Menu.Item key="21">
                            <Link to="/codeexport">
                                <Icon type="key" /><span>代码导出</span>
                            </Link>
                        </Menu.Item>
                    </SubMenu>
                    <SubMenu key="sub9" title={<span><Icon type="setting" /><span>个人管理</span></span>}>
                        <Menu.Item key="91">
                            <Link to="/personal">
                                <Icon type="key" /><span>密码修改</span>
                            </Link>
                        </Menu.Item>
                    </SubMenu>
                </Menu>

            </Sider>
        );
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        changeLocation(locationList){
            dispatch(LocationActionCreator.changeLocation(locationList))
        }
    }
}

export default connect(null,mapDispatchToProps)(SideBar)