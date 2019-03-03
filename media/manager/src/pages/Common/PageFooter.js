import React from "react";
import {Layout} from "antd";

const { Footer } = Layout;

export default class PageFooter extends React.PureComponent {
    render() {
        return (
            <Footer style={{ textAlign:"center",padding: 10 }}>
                ZUA ©2019 郑州航空工业管理学院/计算机技术实验中心
            </Footer>
        )
    }
}