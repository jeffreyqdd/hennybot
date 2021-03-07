#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <random>
#include <chrono>
using namespace std;
// input format
// word, current_guess, guess_letter, num_wrong
namespace fs = std::filesystem;

void generateWord(string path)
{   
    ifstream fin;

    fin.open(path +"/dictionary.txt");

    vector<string> valid_words = vector<string>();
    while(!fin.eof())
    {
        string word; fin >> word;

        if (word.length() > 5)
        {
            valid_words.push_back(word);
        }
    }
    //shuffle
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    shuffle ( valid_words.begin(), valid_words.end(), default_random_engine(seed));

    string currentGuess = "";

    for(int i = 0; i < valid_words[0].length(); i++)
        currentGuess += ".";

    //output format
    //word, current_guess, num_wrong, win/loss/ongoing
    cout << valid_words[0] << " " << currentGuess << " " << 0 <<" "<< "ongoing"
     << endl;
    cout.flush();
    
}

void logic(string answer, string current, string guess, string wrong)
{
    bool flag = false;
    for(int i = 0; i < answer.length(); i++)
    {
        if(answer[i] == guess[0])
        {
            flag = true;
            current[i] = guess[0];
        }
    }
    int num_wrong = stoi(wrong); 
    
    if (!flag)
        num_wrong++;


    bool is_loss = num_wrong >= 6;
    bool is_win = true;

    for(int i = 0; i < answer.length(); i++)
    {
        if(answer[i] != current[i])
        {
            is_win = false;
        }
    }

    string status = "";

    if (is_loss) status = "loss";
    else if(is_win) status = "win";
    else status = "ongoing";

    cout << answer << " " << current << " " << num_wrong <<" "<<status << endl;
    cout.flush();

    //word, current_guess, num_wrong, win/loss/ongoing
}

int main()
{
    string answer;
    string current;
    string guess;
    string wrong;
    string path;

    cin >> answer >> current >> guess >> wrong >> path;

    if (answer == ".")
    {
        generateWord(path);
    }
    else
    {
        logic(answer, current, guess, wrong);
    }
}
