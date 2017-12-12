<template>
  <div class="tagTree">
    <div>
      Current User: {{ this.$route.params.name }}
    </div>

    <div class="block">
      <span class="demonstration">Classification Tree</span>
      <el-cascader
        :options="tree"
        v-model="direc"
        change-on-select="true">
      </el-cascader>
    </div>
    <div>
      Current Class: {{ currentPath.join(': ') }}
    </div>
    <el-button @click=add_class>new class</el-button>
    <el-button @click=add_file>add file</el-button>


    <a v-if=addClass>
      <v-input
        placeholder="input class name"
        v-model="newClass">
      </v-input>
      <v-button
        @click=add_new_class>
        +
      </v-button>
    </a>

    <a v-if=addFile>
    <v-input
      placeholder="input title"
      v-model="newFileTitle">
    </v-input>
    <v-input
      placeholder="input file url"
      v-model="newFileUrl">
    </v-input>
    <v-button
      @click=add_new_file>
      +
    </v-button>
    </a>

    <el-row :span="20">
      <el-col :span="10">
        <el-dialog>File List:</el-dialog>
        <el-table
          :data="fileList"
          height="250"
          border
          style="width: 100%">
          <el-table-column
            prop="title"
            label="Title"
            width="180">
          </el-table-column>
          <el-table-column
            fixed="right"
            label="operation"
            width="100">
            <template slot-scope="scope">
              <el-button @click="view_file(scope.row)" type="text" size="small">
                view
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>

      <el-col :span="10">
        <el-dialog>Detail:</el-dialog>
        <router-link
          :to="{ name: 'showPdf',
               params: {hash_code: file.hash_code}}">
          <el-button> Read Paper! </el-button>
        </router-link>
        <router-link
          :to="{ name: 'fileInfo',
               params: {hash_code: file.hash_code}}">
          <el-button> Change Info </el-button>
        </router-link>

      </el-col>
    </el-row>
  </div>
</template>

<script>
var axios = require('axios');
var qs = require('qs');

export default {

      name: 'tagTree',
      data () {
          return {
              fileInto: {},
              fileList: [],
              userId: "10032",
              tree: [],
              direc: [],
              addClass: false,
              addFile: false,
              newClass: "",
              newFileTitle: "",
              newFileUrl: ""
          }
      },
      methods: {

            showTags () {
                this.$http.get('/api/show_classification_tree?username=' + this.$route.params.name)
                    .then((response) => {
                        var res = response;
                        this.tree = res['node'];
                    })
            },
            showFiles () {
                axios.post('/api/show_paper_of_the_node?username=',
                           qs.stringify({ username: this.userId,
                                          classification_node: this.direc[this.direc.length - 1]})
                          )
                    .then((response) => {
                        var res = JSON.parse(response.bodyText)
                        if (res['error_num'] == 0) {
                            this.fileList = res['papers_title']
                        } else {
                            console.log('Error: cannot get file list!')
                            this.fileList = []
                        }
                    })
            },
            add_class () {
                this.addClass = true;
            },
            add_new_class () {
                axios.post('/api/add_classification',
                           qs.stringify({ username: this.userId,
                                          father_name: this.direc.join('.'),
                                          name: this.newClass})
                          )
                    .then((response) => {
                        if (response["error_num"] == 0) {
                            this.showTags();
                            this.addClass = false;
                        } else {
                            alert(response["msg"]);
                        }
                    });
            },

            add_file () {
                this.addFile = true;
            },
            add_new_file () {
                axios.post('/api/add_paper',
                           qs.stringify({username: this.userId,
                                         title: this.newFileTitle,
                                         url: this.newUrl,
                                         file_path: this.direc.join('/'),
                                         node_name: this.direc[this.direc.length - 1]})
                          )
                    .then((response) => {
                        if (response["error_num"] == 0) {
                            this.showFile();
                            this.addFile = false;
                        } else {
                            console.log(response["msg"]);
                        }
                    })

            },
            view_file (row) {
                var row_title = row["paper_title"];
                axios.post('/api/show_paper_detail',
                           qs.stringify({title: row_title,
                                         username: this.userId})
                          )
                    .then((response) => {
                        if (response["error_num"] == 0) {
                            this.fileInfo = response;
                        } else {
                            console.log(response["msg"]);
                        }
                    })
            }
        },
        mounted: function() {
      //这个是钩子函数
      //如果cartView函数要执行，必须先执行钩子函数
      //这个钩子函数完成了对cratView函数的调用
      //应该注意的是，使用mounted 并不能保证钩子函数中
      // 的 this.$el 在 document 中。为此还应该引入
      // Vue.nextTick/vm.$nextTick
            this.$nextTick(function () {
                this.userId = this.$route.params.name;
                this.showTags()
                this.showFiles()
            })
        }
    }
</script>
