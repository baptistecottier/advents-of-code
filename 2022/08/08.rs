aoc2022::main!(); 

fn generator(input : &str) -> Vec<(u32 , Vec<Vec<u32>>)> {
    let sl = input.lines().count() ; 
    let grid = input.clone()
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap()).collect_vec())
        .flatten()
        .collect_vec();
    
    let h_views = grid.clone()
        .chunks(sl)
        .map(|r| (0..sl).map(|n| { let mut a = r[0..n].to_vec() ;
            a.reverse() ; 
            vec![a , r[n+1..].to_vec()]}).collect_vec())
        .flatten()
        .collect_vec() ;


    let v_views = grid
    .iter()
    .enumerate()
    .sorted_by_key(|(n,_)| (n % sl))
    .map(|(_, c)| *c)
    .collect_vec()
    .chunks(sl) 
    .map(|r| (0..sl).map(|n| { let mut a = r[0..n].to_vec() ;
        a.reverse() ; 
        vec![a ,  r[n+1..].to_vec()]}).collect_vec())
    .flatten()
    .enumerate()
    .sorted_by_key(|(n,_)| (n % sl))
    .map(|(_, c)| c)
    .collect_vec();

    let test = zip(grid.clone(), zip(h_views.clone(), v_views.clone()))
        .map(|(t , (mut hv , mut vv))| {
            hv.append(&mut vv);
            (t, hv) 
})
        .collect_vec() ; 
    test
}

fn part_1(input : Vec<(u32 , Vec<Vec<u32>>)>  ) -> usize {
    input
        .iter()
        .filter(|( size , views )| views.iter().any( |v| v.is_empty() || size > v.iter().max().unwrap()))
        .count()
}

fn part_2(input:  Vec<(u32 , Vec<Vec<u32>>)>  ) -> usize {
    input
        .iter()
        .map(|( size , views )| views.iter().fold(1, |score , l | {
            let mut lview = l.iter().take_while(|t| t < &size).count() ;
            if lview != l.len() {lview += 1} 
            score * lview }
        ))
        .max()
        .unwrap()
}