aoc::main!(); 

fn parser(input: &str) -> Value {
    input.parse().unwrap()
}

fn part_1(loads: Value) -> i64 {
    sum_json(&loads, &json!(""))
}

fn part_2(loads: Value) -> i64 {
    sum_json(&loads, &json!("red"))
}

fn sum_json(loads: &Value, ban_word: &Value) -> i64 {
    match loads {
        Value::Number(n) => n.as_i64().unwrap(),
        Value::Object(o) => if o.values().contains(&ban_word) {0} else {o.iter().map(|l| sum_json(l.1, ban_word)).sum()},
        Value::Array(a)  => a.iter().map(|l| sum_json(l, &ban_word)).sum(),
        Value::String(_) => 0,
        _ => unreachable!(),
    }
}