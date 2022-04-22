mod utils;

use wasm_bindgen::prelude::*;
use serde::{Serialize, Deserialize};
use std::{thread, time::Duration};

#[derive(Serialize, Deserialize)]
pub struct Team {
    pub name: String,
    pub players: Vec<Player>,
}

#[derive(Serialize, Deserialize)]
pub struct Player {
    pub name: String,
	pub position: String,
    pub goals: u32,
	pub assists: u32,
	pub team: Team
}

#[wasm_bindgen]
extern {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn wasm_avg_goals(results: &JsValue){
	thread::sleep(Duration::from_millis(4000));
	utils::set_panic_hook();
	
	alert("working");

	web_sys::console::log_1(&"Modified Example in Rust".into());
	match results.into_serde::<Team>() {
		Ok(mut v) => {

			web_sys::console::log_2(&"Modified Example in Rust".into(), &JsValue::from_serde(&v).unwrap());
		},
		Err(_) => web_sys::console::log_2(&"Could not parse this as an Example:".into(), results)
	}
}
