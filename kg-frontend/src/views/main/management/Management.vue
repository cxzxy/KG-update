<template>
  <div class="user">
    <div class="el-icon-s-tools" @click="haddleSettings"></div>
    <div
      class="userList"
      v-for="(user, index) in user_permissions"
      :key="index"
      style="width: 900px"
    >
      <div class="shouquan">
        <el-button type="text" class="guard" @click="guardAdmin(user.user_id)"
          >授予管理员权限</el-button
        >
      </div>

      <div class="userinfo">
        <ul style="float: left">
          <li class="username">用户名:&nbsp;&nbsp;&nbsp;{{ user.username }}</li>
          <li class="email">邮箱:&nbsp;&nbsp;&nbsp;{{ user.email }}</li>
          <li class="role">
            身份:&nbsp;&nbsp;&nbsp;{{ getIdentity(user.role) }}
          </li>
          <li
            class="ps"
            style="float: left"
            v-for="(permission, index) in user.permission"
            :key="index"
          >
            {{ permission_name[index] }}:&nbsp;&nbsp;&nbsp;
            <el-switch
              v-model="permission.is_allowed"
              active-color="#5e85bf"
              inactive-color="#eef0f4"
            >
            </el-switch>
          </li>
          <li>
            <el-button
              type="primary"
              round
              class="save el-icon-check"
              @click="updatePermission(user.user_id)"
            ></el-button>
          </li>
        </ul>
      </div>
    </div>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="params.currentpage"
      :page-size="params.pageSize"
      layout="prev, pager, next"
      :total="total"
      class="pagination"
    >
    </el-pagination>
    <div class="modal" v-show="visible">
      <div class="el-icon-close close-settings" @click="close_settings"></div>
      <div class="modal-mask"></div>
      <div class="model-container">
        <h3>设置</h3>
        <div class="switch" v-for="(item, index) in settings" :key="index">
          {{ setting_name[index] }}
          <el-switch
            v-model="item.isOpened"
            active-color="#5e85bf"
            inactive-color="#eef0f4"
          >
          </el-switch>
        </div>

        <el-button @click="close" class="settings-save">保存</el-button>
      </div>
    </div>
  </div>
</template>
  <script>
import { getPermission, updatePermission, guardAdmin } from "api/permission";
import { getSettings, updateSettings } from "api/settings";
export default {
  name: "Management",
  components: {},
  data() {
    return {
      user_permissions: [],
      permission_name: ["上传文献", "获取问题答案", "获取知识图谱"],
      total: 0,
      params: {
        currentpage: 1,
        pageSize: 5,
      },
      visible: false,
      settings: [],
      setting_name: ["文献自动审核", "关闭权限管理"],
    };
  },
  computed: {},
  methods: {
    getIdentity(role) {
      return role ? "管理员" : "普通用户";
    },
    updatePermission(userid) {
      let permission = this.user_permissions.filter(
        (item) => item.user_id == userid
      )[0].permission;
      let permissions = [];
      permission.forEach((item) => {
        permissions.push(item.is_allowed ? 1 : 0);
      });
      let permission_id = [1, 2, 3];
      // console.log(permissions);
      updatePermission({
        user_id: userid,
        permission_id: permission_id,
        is_allowed: permissions,
      }).then((res) => {
        if (res.code == 200) {
          this.$message({
            message: "修改成功",
            type: "success",
          });
        }
        else console.log(res);
      });
    },
    guardAdmin(userid) {
      guardAdmin({ user_id: userid }).then((res) => {
        if (res.code == 200) {
          this.$message({
            message: "授权成功",
            type: "success",
          });
          this.getPermission();
        } else console.log(res);
      });
    },
    handleSizeChange(val) {
      this.params.pageSize = val;
      this.getPermission();
    },
    handleCurrentChange(val) {
      this.params.currentpage = val;
      this.getPermission();
    },
    getPermission() {
      getPermission(this.params).then((res) => {
        this.user_permissions = res.data.user_list;
        this.total = res.data.total;
      });
    },
    getSettings() {
      getSettings().then((res) => {
        if (res.code == 200) {
          this.settings = res.data.settings;
          console.log(this.settings);
        }
      });
    },
    updateSettings() {
      updateSettings({
        auto_examine: this.settings[0].isOpened == true ? 1 : 0,
        turn_off_permission_control: this.settings[1].isOpened == true ? 1 : 0,
      }).then((res) => {
        if (res.code == 200) {
          this.$message({
            message: "修改成功",
            type: "success",
          });
        }
        // console.log(res)
      });
    },
    haddleSettings() {
      this.visible = true;
      this.getSettings();
    },
    close() {
      this.visible = false;
      this.updateSettings();
    },
    close_settings() {
      this.visible = false;
    },
  },

  created() {
    this.getPermission();
  },
};
</script>
  <style scoped>
.user {
  margin-left: 20px;
}
.user .userList {
  position: relative;
  width: 700px;
  padding: 0 20px;
  display: flex;
  flex-direction: column;
  /* background: rgba(0,0,0, 0.1); */
}
.username {
  float: left;
  width: 260px;
}
.email {
  float: left;
  width: 300px;
}
.role {
  float: left;
  width: 260px;
}
.permission {
  position: relative;
  height: 70%;
}
.ps {
  float: left;
  margin-right: 40px;
  margin-top: 20px;
}

.el-button--text {
  border-color: transparent;
  color: #409eff;
  background: 0 0;
  padding-left: 0;
  padding-right: 0;
}
.save {
  width: 60px;
  height: 14px;
  margin-top: 20px;
  background-color: #5e85bf;
}
.shouquan {
  position: relative;
  padding: 0;
  left: 750px;
  top: 30px;
  width: 60px;
}
.el-button--primary {
  position: relative;
  left: 250px;
  color: #fff;
  /* background-color: #409eff; */
  /* border-color: #409eff; */
  line-height: 0;
}
.guard {
  color: #5e85bf;
  /* font-size: 14px; */
}
.el-icon-s-tools {
  position: absolute;
  font-size: 40px;
  right: 100px;
  top: 100px;
  color: #5e85bf;
  cursor: pointer;
}
.pagination {
  position: absolute;
  bottom: 80px;
  left: 600px;
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-mask {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: -1;
}

.model-container {
  /* position: absolute; */
  width: 200px;
  height: 200px;
  top: 800px;
  max-width: 800px;
  background-color: #fff;
  border-radius: 10px;
  padding: 20px;
  z-index: 999;
}
.close-settings {
  position: absolute;
  top: 280px;
  right: 646px;
  font-size: 20px;
  z-index: 9999;
  cursor: pointer;
}
.close-settings :hover {
  color: #5e85bf;
}
h3 {
  margin-left: 55px;
  /* margin-top: 20px; */
}
.settings-save {
  margin-top: 20px;
  cursor: pointer;
  margin-left: 40px;
  border-radius: 20px;
  /* background-color: #5e85bf; */
  color: #5e85bf;
}
.switch {
  margin-left: 10px;
  margin-top: 20px;
}
</style>
  