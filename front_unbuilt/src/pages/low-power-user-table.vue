<template>
<el-main class="main-bar">
                <div class="main-header">
                   <el-breadcrumb separator="/">
                    <el-breadcrumb-item>低压用户列表</el-breadcrumb-item>
                    </el-breadcrumb>
                </div>
                <div class="main-action">
                   <el-button icon="el-icon-plus" size="small" style="border:none" @click="handleAdd">
                        <span>添加</span>
                   </el-button>
                   <span class="main-action-span"><i class="el-icon-info"></i>用户总数：{{usercount}}</span>
                   <span class="main-action-span"><i class="el-icon-info"></i>最高日用电量：{{maxdayilyconsumption}}</span>
                   <span class="main-action-span"><i class="el-icon-info"></i>最高日用电异常等级：{{maxdayilygrade}}</span>
                </div>
                <div class="main-content">
                    <el-table :data="tableData" style="width:100%">
                        <el-table-column type="index" width="75px" label="序号">
                        </el-table-column>
                        <el-table-column v-for="(title,index) in tableTitles" :key="index" :label="title.label"
                        :property="title.prop"
                        >
                        </el-table-column>
                        <el-table-column label="操作" width="200px">
                            <template slot-scope="scope">
                                <el-button size="mini" @click="handleDelete(scope.row,scope.$index)" type="danger">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                     <div class="pagination">
                         <el-pagination
                            :page-size="pagesize"
                            background
                            layout="prev, pager, next"
                            :current-page.sync="pageno"
                            :total="total"
                            @current-change="handlePage"
                            >
                         </el-pagination>
                    </div>
                </div>
            </el-main>
</template>

<script>
import Api from '@/Api/low-power-user-config'
export default {
  data () {
    return {
      tableTitles: [
        {
          label: '用户名称',
          prop: 'lowpowerusername'
        }, {
          label: '用户用电量',
          prop: 'lowpowerusereleconsumption'
        }, {
          label: '用户用电异常等级',
          prop: 'lowpoweruserlevel'
        }
      ],
      maxdayilyconsumption: 0,
      usercount: 0,
      maxdayilygrade: 0,
      tableData: [],
      pagecount: 0,
      total: 0,
      pageno: 1,
      pagesize: 8
    }
  },
  created () {
    this.getLowPowerUserList()
  },
  methods: {
    getLowPowerUserList () {
      let formData = new FormData()
      formData.append('pageno', this.pageno)
      formData.append('pagesize', this.pagesize)
      Api.getLowPowerUsers(formData).then(response => {
        this.tableData = response.data
        this.total = response.pagecount
        this.pageno = response.pageno
        this.maxdayilygrade = response.maxdayilygrade
        this.usercount = response.usercount
        this.maxdayilyconsumption = response.maxdayilyconsumption
      }).catch(error => {
        this.$message.error(error.msg || '获取失败')
      })
    },
    handlePage () {
      this.getFaultList()
    },
    postDelete (row, index) {
      let formData = new FormData()
      formData.append('username', row.lowpowerusername)
      Api.lowpoweruserDelete(formData).then(response => {
        this.$message.success('删除成功')
        this.tableData.splice(index, 1)
        this.getLowPowerUserList()
      }).catch(error => {
        this.$message.error('删除失败' || error.msg)
      })
    },
    handleDelete (row, index) {
      const h = this.$createElement
      this.$msgbox({
        title: '删除提示',
        message: h('p', null, [
          h('span', null, '确定删除用户' + row.lowpowerusername + '?')
        ]),
        showCancelButton: true,
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        callback: action => {
          if (action === 'confirm') {
            this.postDelete(row, index)
          }
        }
      })
    },
    handleAdd () {
      this.$router.push({
        path: '/main/lowpowerusersadd'
      })
    }
  }
}
</script>
<style lang="scss" scope>
</style>
