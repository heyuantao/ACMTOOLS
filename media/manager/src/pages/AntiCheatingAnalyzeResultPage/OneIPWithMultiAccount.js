import React from "react";
import {connect} from "react-redux";
import {fromJS} from "immutable";
import {Link,hashHistory} from "react-router";
import * as LocationActionCreator from "../Common/store/LocationIndicatorActionCreator";
import {Button, Col, Row, Table, Tabs, Tag} from "antd";
import Settings from "../../Settings";

const req = Settings.request;
const table_data_api_url = Settings.anti_cheating_contest_api_url;

class OneIPWithMultiAccount extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            contest_id:this.props.contest_id,
            pagination: fromJS({ totalItem: 10, pageSize: 10, pageNumber: 1, needPagination: true }),
            fetching: false,
            tableData: fromJS([]),

        }
    }
    fetchTableListData() {
        const url = table_data_api_url+this.props.contest_id+"/multiaccount/";
        const params = this.state.pagination.toJS();
        this.setState({fetching:true})
        req.get(url, {params:params}).then(function (response) {
            let tableData = fromJS(response.data.items);
            let paginationData = fromJS(response.data.pagination);
            this.setState({pagination:paginationData});
            this.setState({ tableData: tableData });
            this.setState({fetching:false});
        }.bind(this)).catch(function (error) {
            this.setState({fetching:false});
        }.bind(this))
    }
    componentDidMount() {
        this.fetchTableListData();
    }
    tableColumnFormat() {
        let tableColumn = [
            { title: "考试编号", dataIndex: "contest_id", key: "contest_id" },
            { title: "考试名称", dataIndex: "contest_title", key: "contest_title" },
            { title: "地址", dataIndex: "ip", key: "ip" },
            { title: "提交次数", dataIndex: "submit_count", key: "submit_count" },
            { title: "账户数量", dataIndex: "account_count", key: "account_count" },
            {
                title: "状态检查",  key: "summary",
                render: (text, record) => (
                    <div>
                        {(record.account_count>1)&&<Tag color="red">可疑</Tag>}
                        {(record.account_count===1)&&<Tag color="blue">正常</Tag>}
                    </div>
                )
            },
        ]
        return tableColumn;
    }
    handleTableChange(pagination, filters, sorter){
        let newPagination=fromJS(pagination)
        this.setState({pagination:newPagination},()=>{this.fetchTableListData()})
    }
    handleExpandedRowRender(record){
        return (
            <span>
                {
                    record.account_list.map( (item,index)=>{
                        return (<Tag color="magenta" key={index} style={{marginBottom:"5px"}}>
                            {item.account_id}-{item.account_nick}-{item.in_date}
                        </Tag>)
                    })
                }
            </span>
        )
    }
    render() {
        return (
            <div >
                <Table dataSource={this.state.tableData.toJS()} rowKey="id" pagination={this.state.pagination.toJS()}
                       expandedRowRender={this.handleExpandedRowRender}
                       onChange={(pagination, filters, sorter)=>{this.handleTableChange(pagination, filters, sorter)}}
                       columns={this.tableColumnFormat()}
                       loading={this.state.fetching}>
                </Table>
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        //showLocation(locationList){
        //    dispatch(LocationActionCreator.changeLocation(fromJS(["作弊分析","代码提交分析","分析结果"])))
        //}
    }
}

export default connect(null,mapDispatchToProps)(OneIPWithMultiAccount)