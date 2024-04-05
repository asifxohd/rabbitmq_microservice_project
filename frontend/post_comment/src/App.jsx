import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faComment, faPaperPlane } from '@fortawesome/free-solid-svg-icons';

function App() {
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState('');
  const [comments, setComments] = useState({});
  const [newComment, setNewComment] = useState('');

  const handlePostSubmit = () => {
    if (newPost.trim() !== '') {
      const postId = Date.now().toString();
      setPosts([...posts, { id: postId, content: newPost }]);
      setComments({ ...comments, [postId]: [] });
      setNewPost('');
    }
  };

  const handleCommentSubmit = (postId) => {
    if (newComment.trim() !== '') {
      setComments({
        ...comments,
        [postId]: [...comments[postId], newComment],
      });
      setNewComment('');
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="max-w-lg w-full p-8 bg-white rounded shadow-md">
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
