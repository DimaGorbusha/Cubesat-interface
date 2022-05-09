import React from "react";
import '../Styles/CreateTest.css';
import { Form, Button } from 'bootstrap-4-react';
import { CustomInput } from "../Components/CustomInput.jsx";

export const CreateTest = () => {
    return (
        <div className="content">
            <div className="container">
                <h3>Создание теста</h3>
                <div className="preset_test">
                    <CustomInput label="Давление" placeholder="20" type="number" />
                    <CustomInput label="Давление" placeholder="20" type="number" />
                    <CustomInput label="Давление" placeholder="20" type="number" />
                    <CustomInput label="Давление" placeholder="20" type="number" />
                </div>
                <Button id="btn_sign" className="btn_sign" class="btn_sign" style={{width:'fit-content', paddingLeft:'30px', paddingRight:'30px',borderRadius:'20px', fontFamily:'Montserrat-Medium', backgroundColor:'#FF4D00', borderColor:'white', outline:'none'}} primary as="input" type="button" value="Сохранить" />

            </div>

        </div>
    )
}