<template>
<div class="page">
  <div class="head">
     <el-breadcrumb separator="/">
         <el-breadcrumb-item :to="{ name: 'lowPowerUser' }"><el-button style="border:none"><i class="el-icon-back"></i>低压用户列表</el-button></el-breadcrumb-item>
      </el-breadcrumb>
  </div>
  <div class="page">
      <div class="config-container">
        <div class="config-box">
            <div class="config-item">
                <div style="color:gray;margin-bottom:5px;">用户名</div>
                <el-input placeholder="请输入用户名称" v-model="username"></el-input>
            </div>
            <div class="config-item">
                <div style="color:gray;margin-bottom:5px;">用户用电量</div>
                <el-input placeholder="请输入用户用电量" v-model="userConsumption"></el-input>
            </div>
            <div class="config-item">
                <div style="color:gray;margin-bottom:5px;">用户用电异常等级</div>
                <el-input placeholder="请输入用户用电异常等级" v-model="userConsumptionLevel"></el-input>
            </div>
            <div class="config-item">
                <el-button type="danger" @click="handleAdd" class="btnbgcolor">添加</el-button>
            </div>
        </div>
    </div>
  </div>
</div>
</template>

<script>
/* eslint-disable */ 
import Api from '@/Api/low-power-user-config'
export default {
  data () {
    return {
      roles: [
        { roleName: '管理员', roleId: 1 },
        { roleName: '普通用户', roleId: 2 }
      ],
      sexs: [
        { sexName: '男', sexId: 1 },
        { sexName: '女', sexId: 2 }
      ],
      username: '',
      userConsumption: '',
      userConsumptionLevel: ''
    }
  },
  created () {
    let username = this.$route.query.username
    if (username) {
      this.isEdit = true
      this.username = username
      this.email = this.$route.query.email
      this.role = this.$route.query.role
    }
  },
  methods: {
    handleAdd () {
      let formData = new FormData()
      formData.append('lowpowerusername', this.username)
      formData.append('eleconsumption', this.userConsumption)
      formData.append('eleconsumptionlevel', this.userConsumptionLevel)
      Api.insertLowPowerUser(formData).then(response => {
        this.$message.success('添加成功')
      }).catch(error => {
        this.$message.error(error.msg || '添加失败')
      })
    }
  }
}
</script>

<style lang="scss" scope>
.page{
  width: 100%;
  height: 100%;
  margin: 10px auto;
  .head{
    width: 90%;
    margin-left: 2%;
  }
  .page{
    width: 30%;
    .config-container{
      margin: 50px auto;
    .config-box{
        display: flex;
        flex-direction: column;
        .config-item{
            margin:15px 0;
        }
    }
  }
  }
}
</style>
