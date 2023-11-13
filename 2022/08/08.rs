aoc2022::main!(); 

fn preprocessing(input: &str) -> Vec<(u32 , Vec<Vec<u32>>)> {
    let sl = input.lines().count() ; 
    let trees = input.chars().filter_map(|c| c.to_string().parse::<u32>().ok()).collect_vec() ; 
    
    let h_views = trees.chunks(sl)
        .map(|r| (0..sl).map(move |n| vec![rev_slice(&r[0..n]) , r[n+1..].to_vec()]))
        .flatten()
        .collect_vec() ;

    let v_views = (0..sl)
        .map(|n| (0..sl)
            .map(|i| trees.chunks(sl).map(|l| l[i].clone()).collect_vec())
            .map(move |r| vec![rev_slice(&r[0..n]) , r[n+1..].to_vec()]))
        .flatten()
        .collect_vec() ;
  
    zip(trees, zip(h_views, v_views))
        .map(|(t , (hv , vv))| (t , [hv, vv].concat()))
        .collect_vec()
}

fn part_1(input: Vec<(u32 , Vec<Vec<u32>>)>  ) -> usize {
    input
        .iter()
        .filter(|( size , views )| views.iter().any( |v| v.is_empty() || size > v.iter().max().unwrap()))
        .count()
}

fn part_2(input:  Vec<(u32 , Vec<Vec<u32>>)>  ) -> usize {
    input
        .iter()
        .map(|( size , views )| views.iter().fold(1, |score , l | {
            let lview = l.iter().take_while(|t| *t < size).count() ;
            if lview == l.len() {score * (lview)} else {score * (lview + 1)}}))
        .max()
        .unwrap()
}