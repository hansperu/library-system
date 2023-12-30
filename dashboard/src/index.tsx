/* @refresh reload */
import { render } from 'solid-js/web'
import { Router, Route } from '@solidjs/router'
import { Home } from './pages/Home'
import { Login } from './pages/Login'
import { NotFound } from './pages/NotFound'
import { Signup } from './pages/Signup'

import './index.css'

const root = document.getElementById('root')

render(() => (
    <Router>
        <Route path="/" component={Home}/>
        <Route path="/login" component={Login}/>
        <Route path="/signup" component={Signup}/>
        {/* <Route path={"/user/:id"} component={User}/> */}
        <Route path="*404" component={NotFound}/>
    </Router>
), root!)
