use std::io;
use std::io::prelude::*;

fn main() {
    let mut line = 0u64;
    let mut word = 0u64;
    let mut byte = 0u64;

    let stdin = io::stdin();
    for l in stdin.lock().lines() {
        let l = l.unwrap();
        line += 1;
        byte += l.as_bytes().len() as u64 + 1; // newline

        let iter = l.split_whitespace();
        word += iter.count() as u64;
    }

    println!("{} {} {}", line, word, byte);
}
