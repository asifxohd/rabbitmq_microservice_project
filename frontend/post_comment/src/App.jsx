import { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faComment, faPaperPlane } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { BASE_URL_BACKUP, BASE_URL_COMMENT, BASE_URL_POSTS } from './constents';

function App() {
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState('');
  const [comments, setComments] = useState({});
  const [newComment, setNewComment] = useState('');

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await axios.get(`${BASE_URL_POSTS}/posts/`);
        const fetchedPosts = response.data;
        setPosts(fetchedPosts);
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    };

    fetchPosts();
  }, []); 

  const handlePostSubmit = async () => {
    if (newPost.trim() !== '') {
      try {
        const response = await axios.post(`${BASE_URL_POSTS}/posts/`, { content: newPost });
        const newPostData = response.data; 
        setPosts([...posts, newPostData]);
        setNewPost('');
      } catch (error) {
        console.error('Error adding post:', error);
      }
    }
  };

  const handleCommentSubmit = async (postId) => {
    if (newComment.trim() !== '') {
      try {
        const response = await axios.post(`${BASE_URL_COMMENT}/comments/`, { post_id: postId, content: newComment, });
        const newCommentData = response.data; 
        setNewComment('');
      } catch (error) {
        console.error('Error adding comment:', error);
      }
    }
  };

  return (
    <div className=" w-2/3 mx-auto h-screen bg-gray-100 ">
      <div className=" w-full p-8 bg-white rounded shadow-md">
        <h1 className="text-2xl font-bold mb-4">Create a New Post</h1>
        <textarea
          className="w-full border border-gray-300 p-2 mb-4 rounded focus:outline-none focus:border-blue-500"
          placeholder="Write your post here..."
          value={newPost}
          onChange={(e) => setNewPost(e.target.value)}
        />
        <button
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
          onClick={handlePostSubmit}
        >
          <FontAwesomeIcon icon={faPaperPlane} className="mr-2" />
          Post
        </button>
        <div className="mt-8">
          <h2 className="text-xl font-bold mb-4">Posts</h2>
          {posts.map((post) => (
            <div key={post.id} className="bg-gray-200 rounded p-4 mb-4">
              <p>{post.content}</p>
              <div className="mt-2">
                <input
                  type="text"
                  className="border border-gray-300 p-2 rounded focus:outline-none focus:border-blue-500"
                  placeholder="Add a comment..."
                  value={newComment}
                  onChange={(e) => setNewComment(e.target.value)}
                />
                <button
                  className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded ml-2"
                  onClick={() => handleCommentSubmit(post.id)}
                >
                  <FontAwesomeIcon icon={faComment} className="mr-2" />
                  Comment
                </button>
                <div className="mt-2">
                  {comments[post.id] &&
                    comments[post.id].map((comment, index) => (
                      <div key={index} className="bg-gray-100 rounded p-2 mb-2">
                        <p>{comment}</p>
                      </div>
                    ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
