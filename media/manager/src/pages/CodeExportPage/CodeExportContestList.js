import React from "react";
import {hashHistory, Link} from "react-router";
import { Row, Col, Form, Button, Table, Icon, Divider} from 'antd';
import { fromJS } from "immutable";
import Settings from "../../Settings";

const FormItem = Form.Item;
const req = Settings.request;
const table_data_api_url = Settings.code_exprot_contest_api_url;

class CodeExportContestList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fetching: false,
            pagination: fromJS({ total: 0, pageSize: 8, current: 1}),
            tableData: fromJS([]),
        }
    }
    componentWillReceiveProps(props) {
        this.fetchTableListData()
    }
    fetchTableListData() {
        const url = table_data_api_url;
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
        this.fetchTableListData()
    }
    handleTableChange(pagination, filters, sorter){
        let newPagination=fromJS(pagination)
        this.setState({pagination:newPagination},()=>{this.fetchTableListData()})
    }
    handleGenerateCodeZipFile(contest_id){
        const url = table_data_api_url+contest_id+"/";
        const params = {'status':'pending'};
        req.put(url, {params:params}).then(function (response) {
            this.fetchTableListData();
        }.bind(this)).catch(function (error) {
        }.bind(this))
    }
    handleDownloadExportCode(contest_id){
        window.location = table_data_api_url+contest_id+"/zip";
    }
    tableColumnFormat() {
        let tableColumn = [
            { title: "考试编号", dataIndex: "contest_id", key: "contest_id" },
            { title: "考试名称", dataIndex: "title", key: "title" },
            { title: "更新时间", key: "in_date",
                render: (text, record) => (
                    <div>
                        {(record.status!=='none')&&<span>{record.in_date}</span>}
                        {(record.status==='none')&&<span>未就绪</span>}
                    </div>
                )
            },
            {
                title: "数据处理状态",  key: "status" ,
                render: (text, record) => (
                    <div>
                        {(record.status==='none')&&<Icon type="question-circle" theme="twoTone" twoToneColor="#eb2f96" />}
                        {(record.status==='pending')&&<Icon type="sync" spin/>}
                        {(record.status==='finished')&&<Icon type="check-circle" theme="twoTone" twoToneColor="#52c41a"/>}
                        {(record.status==='error')&&<Icon type="question-circle" theme="twoTone" twoToneColor="#eb2f96" />}
                    </div>
                )
            },
            {
                title: "状态描述", key: "action",
                render: (text, record) => (
                    <div>
                        {(record.status==='pending')&&<a disabled={true}>下载文件</a>}
                        {
                            (record.status==='finished')&&
                            <span>
                                <a onClick={()=>{this.handleDownloadExportCode(record.contest_id)}}>下载文件</a>
                                <Divider type="vertical" />
                                <a onClick={()=>{this.handleGenerateCodeZipFile(record.contest_id)}}>重新生成</a>
                            </span>
                        }
                        {
                            (record.status==='error')&&
                            <span>
                                <a  onClick={()=>{this.handleGenerateCodeZipFile(record.contest_id)}}>重新生成</a>
                            </span>}
                        {
                            (record.status==='none')&&
                            <span>
                                <a onClick={()=>{this.handleGenerateCodeZipFile(record.contest_id)}}>开始生成</a>
                            </span>
                        }
                    </div>
                )
            },
        ];
        return tableColumn;
    }
    handleFetchTableData(){
        this.fetchTableListData()
    }
    render() {
        return (
            <div>
                <Row type="flex" justify="space-between" align="middle" >
                    <Col>
                        <h2>代码导出管理</h2>
                    </Col>
                    <Col>
                        <Button onClick={() => { this.handleFetchTableData() }} type="primary" >刷新</Button>
                    </Col>
                </Row>
                <Row type="flex" justify="space-between" align="middle">
                    <Col span={24}>
                        <div style={{ marginBottom: "15px" }}></div>
                        <Table dataSource={this.state.tableData.toJS()} rowKey="id" pagination={this.state.pagination.toJS()}
                            onChange={(pagination, filters, sorter)=>{this.handleTableChange(pagination, filters, sorter)}}
                            columns={this.tableColumnFormat()}
                            loading={this.state.fetching}
                        ></Table>
                    </Col>
                </Row>
            </div>
        )
    }
}

export default CodeExportContestList