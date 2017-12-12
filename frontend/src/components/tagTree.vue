<template>
  <div class="tagTree">
    <el-container style="text-align: left; background-color: rgb(238, 241, 246); fontSize:18px">
      <el-header style="height:60px">
        <el-row>
          <el-col :span="3">
            <div>
              Current User: {{ this.$route.params.name }}
            </div>
          </el-col>
          <el-col :span="7">
            <div class="block">
              <span class="demonstration">Classification Tree</span>
              <el-cascader
                :options="tree"
                v-model="direc"
                change-on-select="true">
              </el-cascader>
              <el-button @click=showFiles> Show </el-button>
            </div>
          </el-col>
          <el-col :span="5">
            <div>
              Current Class: {{ direc.join(': ') }}
            </div>
          </el-col>

          <el-col :span="1.5">
            <el-popover
              ref="popoverClass"
              placement="right"
              width="300"
              trigger="click">
              <el-input
                style="width:83%;"
                placeholder="input class name"
                v-model="newClass">
              </el-input>
              <el-button
                @click=add_new_class>
                +
              </el-button>
            </el-popover>
            <el-button v-popover:popoverClass>new class</el-button>
          </el-col>
          <el-col :span="1.5">
            <el-popover
              ref="popoverFile"
              placement="right"
              width="300"
              trigger="click">
              <el-input
                placeholder="input title"
                v-model="newFileTitle">
              </el-input>
              <el-input
                placeholder="input file url"
                v-model="newFileUrl">
              </el-input>
              <el-button
                @click=add_new_file>
                +
              </el-button>
            </el-popover>
            <el-button v-popover:popoverFile> new file</el-button>
          </el-col>
        </el-row>
        
      </el-header>

      <el-container>
        <el-aside width="600px" style="background-color: rgb(238, 241, 246);fontSize:15px">
          
                    
          <p>File List:</p>
          <el-table
            :data="fileList"
            height="800"
            border
            style="width: 100%">
            <el-table-column
              prop="paper_title"
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
      </el-aside>


      <el-main>
          <div>
          <p>
            title: {{ fileInfo.title }}
          </p>
          <p>
            author:
          <ul v-for="author in fileInfo.author">
            <li>
              {{author.first_name}}, {{author.last_name}}  email: {{author.email}}
            </li>
          </ul>
          </p>
          <p>
            publish time: {{fileInfo.publish_time}}
          <p>
            url: {{ fileInfo.url }}
          </p>
          <p>
            source: {{fileInfo.source}}
          <p>
            read status: {{ fileInfo.read_status }}
          </p>
          
          <router-link
            :to="{ name: 'showPdf',
                 params: {hash_code: fileInfo.hash_code}}">
            <el-button> Read Paper! </el-button>
          </router-link>
          <router-link
            :to="{ name: 'fileInfo',
                 params: {hash_code: fileInfo.hash_code}}">
            <el-button> Change Info </el-button>
          </router-link>
          </div>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
var axios = require('axios');
var qs = require('qs');

export default {

      name: 'tagTree',
      data () {
          return {
              fileInfo: {},
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
                this.$http.get("/api/show_classification_tree?username=" + this.$route.params.name)
                    .then((response) => {
                        var res = response.data;
                        this.tree = res['node'];
                    })
            },
            showFiles () {
                axios.post('/api/show_paper_of_the_node',
                           qs.stringify({ username: this.userId,
                                          classification_node: this.direc[this.direc.length - 1]})
                          )
                    .then((response) => {
                        var res = response.data;
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
                    .then((responses) => {
                        var response = responses.data;
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
                                         links: this.newFileUrl,
                                         file_path: this.direc.join('/'),
                                         node_name: this.direc[this.direc.length - 1]})
                          )
                    .then((response) => {
                        if (response.data["error_num"] == 0) {
                            this.showFiles();
                            this.addFile = false;
                        } else {
                            console.log(response.data["msg"]);
                        }
                    })
            },
            view_file (row) {
                var row_title = row["paper_title"];
                axios.post('/api/show_paper_detail',
                           qs.stringify({title: row.title,
                                         hash_code: row.hash_code,
                                         username: this.userId})
                          )
                    .then((response) => {
                        if (response.data["error_num"] == 0) {
                            this.fileInfo = response.data;
                        } else {
                            console.log(response.data["msg"]);
                        }
                    })
            }
        },
        mounted: function() {
            this.$nextTick(function () {
                this.userId = this.$route.params.name;
                this.showTags()
            })
        }
    }
</script>
