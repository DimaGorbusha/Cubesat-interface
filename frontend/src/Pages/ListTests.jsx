import React from "react";
import "../Styles/ListTests.css";
import { Form, Button } from 'bootstrap-4-react';

export const ListTests = () => {
    return (
        <div className="content">
            <div className="labels">
                <div>
                    <h2 style={{ fontFamily: 'Montserrat-Bold' }}>Вы в режиме <h2 style={{ color: '#FF4D00' }}>инженера-испытателя</h2></h2>
                    <p>Вы имеете право управлять, создавать и редактировать испытания</p>
                </div>
                <Button id="btn_sign" className="btn_sign" class="btn_sign" style={{ width: 'max-content', paddingLeft: '50px', paddingRight: '50px', marginLeft: 'auto', height: 'fit-content', borderRadius: '20px', fontFamily: 'Montserrat-Medium', backgroundColor: '#FF4D00', borderColor: 'white', outline: 'none' }} primary as="input" type="button" value="Создать тест" />


            </div>
            <div>

            </div>


        </div>
    )
}