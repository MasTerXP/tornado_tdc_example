#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class TutorialGETHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        input = kwargs.get('only_number')
        self.write("This is number "+input)

class TutorialPOSTHandler(tornado.web.RequestHandler):
    def post(self):
        message = json.loads(self.request.body)
        print message.get('data')

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/argument_get_tutorial/(?P<only_number>[[0-9]+)", TutorialGETHandler),
        (r"/argument_post_tutorial", TutorialPOSTHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print "Start Tornado server at Port:"+options.port
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
